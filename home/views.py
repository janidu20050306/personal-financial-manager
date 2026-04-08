from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Expense


# Create your expenses here.
@login_required(login_url='/login/')
def home(request):
    salary = 0
    if request.method == "POST":
        data = request.POST
        salary = data.get('salary') or 0
        name = data.get('name')
        price = int(data.get('price'))

        Expense.objects.create(user=request.user,
                               salary=salary,
                               name=name,
                               price=price)

        return redirect('/')

    queryset = Expense.objects.all()
    if request.GET.get('search'):
        queryset = queryset.filter(name__icontains=request.GET.get('search'))

    # calculate total expenses
    total_sum = sum(expense.price for expense in queryset)
    context = {
        'expenses': queryset,
        'total_sum': total_sum
    }
    return render(request, 'home/home.html', context)


# update an expense data
@login_required(login_url='/login/')
def update_expense(request, id):
    query = Expense.objects.get(id=id)
    if request.method == "POST":
        data = request.POST
        salary = data.get('salary') or 0
        name = data.get('name')
        price = int(data.get('price'))

        query.user = request.user
        query.salary = salary
        query.name = name
        query.price = price
        query.save()

        return redirect('/')

    context = {
        'expense': query
    }
    return render(request, 'home/update_expense.html', context)


# delete an expense data
@login_required(login_url='/login/')
def delete_expense(request, id):
    query = Expense.objects.get(id=id)
    query.delete()
    return redirect('/')


# login page for user
def login_view(request):
    if request.method == "POST":
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_obj = User.objects.filter(username=username).first()
            if not user_obj:
                messages.error(request, 'User not found')
                return redirect('/login/')
            user_auth = authenticate(username=username, password=password)
            if user_auth:
                auth_login(request, user_auth)
                return redirect('home')
            messages.error(request, 'Invalid credentials')
            return redirect('/login/')
        except Exception as e:
            messages.error(request, 'Something went wrong')
            return redirect('/login/')
    return render(request, 'home/login.html')


# registration page for user
def register(request):
    if request.method == "POST":
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_obj = User.objects.filter(username=username).first()
            if user_obj:
                messages.error(request, 'Username already exists')
                return redirect('/register/')
            user_obj = User.objects.create(username=username)
            user_obj.set_password(password)
            user_obj.save()
            messages.success(request, 'User created successfully')
            return redirect('/login/')
        except Exception as e:
            messages.error(request, 'Something went wrong')
            return redirect('/register/')
    return render(request, 'home/register.html')


# login function 
def custom_login(request):
    auth_logout(request)
    return redirect('/login/')


# generate the bill for the user
@login_required(login_url='/login/')
def pdf(request):
    if request.method == "POST":
        data = request.POST
        salary = data.get('salary') or 0
        name = data.get('name')
        price = int(data.get('price'))

        expense = Expense.objects.create(user=request.user,
                                         salary=salary,
                                         name=name,
                                         price=price)
        return redirect('/pdf/')
    queryset = Expense.objects.all()
    if request.GET.get('search'):
        queryset = queryset.filter(name__icontains=request.GET.get('search'))

    # calculate total expenses
    total_sum = sum(expense.price for expense in queryset)

    # get the template
    username = request.user.username
    context = {
        'expenses': queryset,
        'total_sum': total_sum,
        'username': username
    }
    return render(request, 'home/pdf.html', context)

