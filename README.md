# Personal Financial Manager

A Django-based web application to track and manage personal expenses. This app helps users record, update, and visualize their spending habits.

## Features

- **User Authentication**: Secure login and registration system
- **Expense Tracking**: Add, edit, and delete expenses
- **Expense Summary**: View total expenses and expense breakdown
- **PDF Export**: Generate and print expense reports
- **Responsive Design**: Bootstrap-based UI for mobile and desktop

## Technologies Used

- **Backend**: Django 4.2.28
- **Database**: SQLite (default)
- **Frontend**: HTML, CSS, Bootstrap 5
- **Authentication**: Django built-in User model

## Project Structure

```
personal-financial-manager/
├── core/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── home/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   ├── templates/home/
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── update_expense.html
│   │   └── pdf.html
│   └── migrations/
├── manage.py
└── requirements.txt
```

## Installation

### Prerequisites

- Python 3.8+
- pip (Python package manager)

### Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/janidu20050306/personal-financial-manager.git
   cd personal-financial-manager/core
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser** (optional, for admin panel):
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

   The app will be available at `http://127.0.0.1:8000/`

## Usage

### Register
- Go to `http://127.0.0.1:8000/register/`
- Create a new account with username and password

### Login
- Go to `http://127.0.0.1:8000/login/`
- Enter your credentials

### Add Expenses
- On the home page, enter expense name and amount
- Click "Submit" to save

### View & Edit Expenses
- All expenses are displayed in a table
- Click "Edit" to modify an expense
- Click "Delete" to remove an expense

### View Summary
- Click "Total Expenses" to see a summary
- Use the Print button to save as PDF

### Logout
- Click "Logout" to end your session

## Database Models

### Expense Model
```python
class Expense(models.Model):
    user = ForeignKey(User, on_delete=SET_NULL, null=True, blank=True)
    salary = IntegerField(default=0, null=True, blank=True)
    name = CharField(max_length=100)
    price = IntegerField(default=0)
```

## API Endpoints

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET, POST | Home page - list and add expenses |
| `/expenses` | GET | Expenses page (alias for home) |
| `/update/<id>` | GET, POST | Update expense |
| `/delete/<id>` | GET | Delete expense |
| `/login/` | GET, POST | User login |
| `/register/` | GET, POST | User registration |
| `/logout/` | GET | User logout |
| `/pdf/` | GET | View expense summary |
| `/admin/` | GET | Django admin panel |

## Deployment

### PythonAnywhere
1. Sign up at pythonanywhere.com
2. Create a new web app
3. Configure to use your GitHub repo
4. Set up virtual environment and install requirements
5. Configure WSGI file

### Heroku
```bash
git push heroku main
```

### Render
1. Connect your GitHub repository
2. Set environment variables
3. Deploy

## Environment Variables

For production, create a `.env` file:
```
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=yourdomain.com
DATABASE_URL=postgresql://user:password@localhost/dbname
```

## Future Enhancements

- Email notifications for budget alerts
- Category-based expense filtering
- Monthly/yearly expense reports
- Charts and graphs visualization
- Multi-currency support
- Export to CSV/Excel
- Mobile app version

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is open source and available under the MIT License.

## Support

For issues or questions, please create an issue on the GitHub repository.

## Author

Created by Janidu induwara  

---

**Note**: This is a personal project for learning Django. For production use, add proper security measures like HTTPS, environment variables for secrets, and comprehensive error handling.
