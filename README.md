# INTERN Assignment

## Features
- Django REST API with JWT authentication
- User registration (web & API)
- Celery background tasks with Redis
- Telegram bot integration

## Setup Instructions

1. **Clone the repo:**
   ```
   git clone https://github.com/samuelbaiju/kanhaiya-intern-assignment.git
   cd project
   ```

2. **Create and activate a virtual environment:**
   ```
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   - Create a `.env` file with:
     ```
     SECRET_KEY=your_secret_key
     DEBUG=True
     EMAIL_HOST_USER=your_email
     EMAIL_HOST_PASSWORD=your_email_password
     CELERY_BROKER_URL=redis://localhost:6379/0
     ```

5. **Run migrations:**
   ```
   python manage.py migrate
   ```

6. **Start Redis server** (see README for platform-specific instructions).

7. **Run Celery worker:**
   ```
   celery -A project worker --pool=solo --loglevel=info
   ```

8. **Run the Django server:**
   ```
   python manage.py runserver
   ```

9. **Run the Telegram bot:**
   ```
   python telegram_bot.py
   ```

## Email Backend

By default, this project uses Django’s **console email backend** for development and testing.  
All emails (such as registration confirmation or Celery task emails) will be printed in your terminal/console instead of being sent to a real email address.

**Current setting in `settings.py`:**
```python
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

### To send real emails via SMTP:

1. **Change the `EMAIL_BACKEND` in your `settings.py` to:**
    ```python
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.gmail.com'  # Or your email provider's SMTP server
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_HOST_USER = 'your_email@example.com'
    EMAIL_HOST_PASSWORD = 'your_email_password_or_app_password'
    DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
    ```
2. **Restart your Django server and Celery worker.**

**Note:**  
- For Gmail, you may need to use an [App Password](https://support.google.com/accounts/answer/185833?hl=en).
- Never commit your real email credentials to version control.
- Always keep your credentials secure (use environment variables or a `.env` file).

## Environment Variables Used

- `SECRET_KEY`
- `DEBUG`
- `DATABASE_NAME`
- `DATABASE_USER`
- `DATABASE_PASSWORD`
- `DATABASE_HOST`
- `DATABASE_PORT`
- `EMAIL_HOST_USER`
- `EMAIL_HOST_PASSWORD`
- `CELERY_BROKER_URL`
- `CELERY_RESULT_BACKEND`

This project uses [python-decouple](https://github.com/henriquebastos/python-decouple) for environment variable management.  
All sensitive configuration should be placed in a `.env` file (see above for an example).

## API Documentation

- `/api/register/` – Register a new user (POST)
- `/api/token/` – Obtain JWT token (POST)
- `/private/` – Protected endpoint (GET, JWT required)
- `/public/` – Public endpoint (GET)
- `/register/` – Web registration page
- `/login/` – Web login page
The login does not redirect[just a page to to check user credentials]

## Telegram Bot

- Start the bot and send `/start` to register your Telegram username.

---

## 7. **Push README.md and Future Changes**

```sh
git add README.md
git commit -m "Add detailed README with setup and API docs"
git push
```

---

## 8. **Commit Regularly**

- Make small, meaningful commits as you work.
- Write clear commit messages.

---

**Summary:**  
- Initialize git, add `.gitignore`, commit, push to GitHub.
- Write a detailed `README.md` with setup, env vars, run instructions, and API docs.
- Keep your code and commit history clean and well-documented.
########
