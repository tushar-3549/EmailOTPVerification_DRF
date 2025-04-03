### OTP Verification via Email in Django

- This project implements OTP (One-Time Password) verification via email using Django. It includes user authentication, email verification, and OTP-based security.

### Features
- User registration with email authentication
- OTP generation and email sending using Django's send_mail
- Verification of OTP to activate users
- Custom user model with email as the unique identifier

### Tech Stack

- Django REST Framework (DRF)

- SMTP for email sending

***Installation & Setup***

- Clone the Repository

git clone https://github.com/tushar-3549/EmailOTPVerification_DRF.git
cd EmailOTPVerification_DRF

- Create and Activate a Virtual Environment
```
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

- Run Migrations

```python manage.py makemigrations
python manage.py migrate
```
- Create a Superuser

`python manage.py createsuperuser`

- Run the Development Server

`python manage.py runserver`


1. Send OTP to Email

- Endpoint: POST 
```
{
    "email": "user@example.com"
}
```
2. Verify OTP

- Endpoint: POST 
```
{
    "email": "user@example.com",
    "otp": "1234"
}
```
