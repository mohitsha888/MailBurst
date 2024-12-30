# **MailBurst**

MailBurst is a Django-based application designed to streamline email campaign management. With features like user authentication, customizable templates, and email scheduling, MailBurst ensures a seamless experience for businesses and individuals aiming to manage email outreach effectively.

---

## **Features**

- **User Authentication**:
  - Secure email-based registration and login.
  - Password management and recovery.

- **Email Campaign Management**:
  - Create and organize contact lists.
  - Schedule and send email campaigns with ease.

- **Customizable Templates**:
  - Build reusable and responsive email templates.

- **Scalable Design**:
  - Built with Django to ensure scalability and robustness.
  - User-friendly, responsive interface.

---

## **Installation**

### **Prerequisites**
- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)
- Git (optional, for cloning the repository)

### **Setup Instructions**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/mohitsha888/MailBurst.git
   cd MailBurst
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the Database**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a Superuser** (optional for admin access):
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the Application**:
   Visit `http://127.0.0.1:8000` in your browser.

---

## **File Structure**

```plaintext
MailBurst/
├── mailburst/               # Project-wide settings and configuration
│   ├── settings/            # Environment-specific settings
│   │   ├── base.py
│   │   ├── production.py
│   │   └── development.py
│   ├── urls.py              # Root URL configuration
│   ├── wsgi.py              # WSGI entry point
│   └── asgi.py              # ASGI entry point
├── apps/                    # Application-specific logic
│   ├── core/                # Shared utilities
│   ├── emails/              # Email campaign management
│   │   ├── tasks.py         # For scheduled tasks (e.g., Celery integration)
│   └── accounts/            # User authentication and profiles
├── static/                  # Static files
│   ├── css/
│   └── js/
├── templates/               # HTML templates
│   ├── base.html
│   ├── core/
│   ├── emails/
│   └── accounts/
├── media/                   # Media files (e.g., attachments)
├── manage.py                # Django management script
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

---

## **Usage**

- **Register**: Create an account via the registration page.
- **Login**: Access your dashboard with your credentials.
- **Dashboard**: Manage contact lists, email campaigns, and templates.
- **Admin Panel**: Visit `/admin/` for advanced management (requires superuser access).

---

## **Contributing**

Contributions are welcome! Follow these steps:

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Make and commit your changes:
   ```bash
   git commit -m "Description of feature or fix"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Submit a pull request on GitHub.

---

## **License**

This project is currently unlicensed. Future licensing decisions will be updated here.

---

## **Contact**

For questions or feedback, reach out:

- **Name**: Mohit Sharma
- **Email**: [themohitsha@gmail.com](mailto:themohitsha@gmail.com)
- **GitHub**: [mohitsha888](https://github.com/mohitsha888)
