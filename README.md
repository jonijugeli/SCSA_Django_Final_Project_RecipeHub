# SCSA_Django_Final_Project_RecipeHub
Users register (by email), create/publish recipes, delete ingredients, remove/add tags, write comments, favorites. Some pages are for authorized users only.

## 🚀 Features

- **User:**
  - Register with email
  - Login / Logout
  - Profile management (bio, phone)
- **Recipes:**
  - Create, edit, delete recipes
  - Automatic assignment of the author
  - Automatic timestamp for creation
- **Notifications:** success messages for registration, login, logout, and profile updates
- **Custom User Model** (email-based authentication)

---

## 📁 Project Structure


---

## 🌐 URLs

| URL                     | Description                       |
|-------------------------|-----------------------------------|
| `/users/register/`      | Registration page                 |
| `/users/login/`         | Login page                        |
| `/users/logout/`        | Logout                             |
| `/users/profile/`       | Profile page                       |
| `/`                     | Homepage with recipe list          |
| `/create/`              | Add a new recipe                   |
| `/update/<id>/`         | Edit a recipe                      |
| `/delete/<id>/`         | Delete a recipe                    |

---

## 🛠 Technologies

- Python 3.11
- Django 5.x
- Bootstrap 5
- SQLite
- Pytest (for testing)

---

## ⚡ Installation

1. **Clone the repository:**
```bash
git clone <repo-url>
cd SCSA_Django_Final_Project_RecipeHub

python -m venv env
# Windows
env\Scripts\activate
# Linux/macOS
source env/bin/activate

pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser
