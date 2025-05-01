# 🏥 Health Care - Hospital Management System (Django)

A Django-based web application for managing hospital operations. Patients can register, book appointments, and contact staff, while admins can assign doctors, manage admissions, and maintain complete patient records. The system features automated email notifications and a user-friendly interface.

---

## 🚀 Features

### 👨‍⚕️ Patient Side
- ✅ Patient Signup/Login
- ✅ Book Appointments
- ✅ Submit Contact Form (with Email Notification)
- ✅ View Appointment & Doctor Assignment
- ✅ Password Reset via Email

### 🛠️ Admin Panel
- ✅ Login & Dashboard
- ✅ Approve/Reject Patient Registrations
- ✅ Assign Doctors with Time & Date
- ✅ Edit/Delete Appointments
- ✅ Admit or Discharge Patients
- ✅ View Patient Records

### 📧 Email Notifications
- 📬 Appointment Confirmation
- 📬 Doctor Assignment
- 📬 Contact Form Response
- 📬 Password Reset Link

### 🎨 UI
- ✅ Responsive and Modern Interface (HTML/CSS/JS/Bootstrap)

---

## 🛠️ Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Django (Python)
- **Database**: SQLite
- **Email**: Django Email Backend with SMTP (e.g., Gmail)
- **Deployment**: Localhost (Deployable to Heroku, Render, etc.)

---

## 📸 Screenshots

> _You can add screenshots of the patient dashboard, admin panel, appointment booking, etc._

---

## 🔧 Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

### Setup Instructions

```bash
# 1. Clone the repository
git clone https://github.com/Ankit-rajan/Health-Care-Ankit.git
cd Health-Care-Ankit

# 2. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate   # On Windows
# source venv/bin/activate  # On macOS/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run database migrations
python manage.py makemigrations
python manage.py migrate

# 5. Create superuser (admin)
python manage.py createsuperuser

# 6. Start the server
python manage.py runserver




✉️ Email Configuration
Add the following in settings.py to enable email functionality:

python
Copy
Edit
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'
⚠️ If using Gmail, enable 2-step verification and generate an App Password for secure authentication.



🗂️ Project Structure
csharp
Copy
Edit
HospitalManagement_Django/
│
├── hospital/            # Core Django app
├── templates/           # HTML templates
├── static/              # CSS/JS/Images
├── db.sqlite3           # SQLite Database
├── manage.py            # Django Management Script
├── requirements.txt     # Dependencies
└── .gitignore           # Git exclusions
🤝 Contributing
Pull requests are welcome. For significant changes, please open an issue first to discuss what you'd like to change.



📄 License
This project is licensed under the MIT License. See the LICENSE file for more details.

🙋‍♂️ Author
Ankit
Roll No: 2203002024
6th Semester, BCA
[GitHub Profile](https://github.com/Ankit-rajan)