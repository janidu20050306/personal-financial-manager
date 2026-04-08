from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('expenses', views.home, name='expenses'),
    path('update/<int:id>', views.update_expense, name='update'),
    path('delete/<int:id>', views.delete_expense, name='delete'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.custom_login, name='logout'),
    path('pdf/', views.pdf, name='pdf'),
]
