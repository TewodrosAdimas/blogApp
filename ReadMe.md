---

# Django Blog and User Management System

This is a Django-based blog application that includes user registration, authentication, profile management, blog post creation, comment management, and a search feature. It also uses **Django-taggit** for tag management.

## Features

1. **User Management**:
   - User Registration, Login, Logout.
   - Profile Management (profile picture and bio).
   - Password change functionality.

2. **Blog Management**:
   - Create, view, edit, and delete blog posts.
   - Add tags to posts using Django-taggit.
   - Paginated post list view.

3. **Comment Management**:
   - Add, edit, and delete comments.
   - View comments associated with each post.

4. **Search**:
   - Search posts by title, content, or tags.

## Prerequisites

- Python 3.8+
- Django 4.0+
- A virtual environment (recommended).
- Database: SQLite (default) or any supported by Django.
- **django-taggit** package installed.

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/TewodrosAdimas/blogApp.git
cd blogApp
```

### 2. Set Up the Virtual Environment

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Collect Static Files

```bash
python manage.py collectstatic
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser.

## Project Structure

```
project-root/
│
├── blog/
│   ├── templates/
│   │   ├── registration/
│   │   │   ├── login.html
│   │   │   ├── signup.html
│   │   │   ├── profile.html
│   │   │   ├── password_change.html
│   │   ├── blog/
│   │   │   ├── post_list.html
│   │   │   ├── post_detail.html
│   │   │   ├── post_form.html
│   │   │   ├── post_delete.html
│   │   │   ├── comment_form.html
│   │   │   ├── comment_delete.html
│   │   │   ├── post_search.html
│   ├── static/
│   │   ├── css/
│   │   │   ├── styles.css
│   │   ├── js/
│   │   │   ├── scripts.js
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│
├── manage.py
├── db.sqlite3
├── requirements.txt
└── README.md
```

## Key Functionalities

### 1. User Authentication

- **Signup**: `/register/`
- **Login**: `/login/`
- **Logout**: `/logout/`

### 2. Blog

- **List Posts**: `/post/`
- **View Post Details**: `/post/<id>/`
- **Create Post**: `/post/new/` (Login required)
- **Edit Post**: `/post/<id>/edit/` (Author only)
- **Delete Post**: `/post/<id>/delete/` (Author only)

### 3. Comments

- **Add Comment**: `/post/<post_id>/comments/new/` (Login required)
- **Edit Comment**: `/post/<post_id>/comment/<id>/update/` (Author only)
- **Delete Comment**: `/post/<post_id>/comment/<id>/delete/` (Author only)

### 4. Profile

- **View Profile**: `/accounts/profile/`
- **Update Profile**: `/registration/profile/`

### 5. Search

- **Search Posts**: `/search/?q=<query>`

## Customization

- Templates and static files are stored in the `templates` and `static` directories. Update `styles.css` and `scripts.js` to modify the UI.
- Extend or customize the models, forms, and views as needed.

## Built With

- **Django**: A high-level Python web framework.
- **Django-taggit**: For tag management.

## Contributing

Contributions are welcome! Fork the repository and submit a pull request for review.

## License

This project is open-source and available under the MIT License.

---
