# 🐱 Cat Collector Django CRUD App – Final Notes

## 🧠 Concepts Covered

### 🛠 Setup
- Installed Django using Pipenv
- Created project using `django-admin startproject catcollector .`
- Created and registered `main_app` using `python manage.py startapp main_app`
- Set up PostgreSQL and configured `settings.py` to connect to a `catcollector` DB

### 🌐 URL Routing
- Project-level `urls.py` includes `main_app.urls`
- `main_app/urls.py` defines view paths (home, about, cats, toys, etc.)

### 🎨 Templates
- Used Django Template Language (DTL) in HTML
- Created `base.html` layout and extended it in `home.html`, `about.html`, etc.
- Dynamic rendering using `{{ variable }}` and `{% for %}`, `{% if %}` blocks

### 📁 Static Files
- Static folders for `css`, `images`, and `js`
- Loaded with `{% load static %}` and linked via `{% static 'path/to/file' %}`

### 🧩 Models
- `Cat`, `Feeding`, and `Toy` models with proper field types
- One-to-many: `Feeding` has `cat = models.ForeignKey(Cat, on_delete=models.CASCADE)`
- Many-to-many: `Cat` has `toys = models.ManyToManyField(Toy)`

### 🧪 ORM Operations
- Used `python manage.py shell` to create and query model instances
- Accessed `Cat.objects.all()`, `Cat.objects.get()`, `Cat.objects.filter()` etc.

### 🛠 Class-Based Views (CBVs)
- Used `ListView`, `DetailView`, `CreateView`, `UpdateView`, `DeleteView` for CRUD
- `get_absolute_url()` for redirecting after create/update
- Templates follow naming conventions like `cat_form.html`, `cat_confirm_delete.html`

### 🐾 Features
- Add/Edit/Delete Cats and Toys
- Track and display Feedings per Cat with a form and table
- Custom feeding status method: `fed_for_today()` checks if cat has full meals
- Added Toy associations via many-to-many with form buttons on detail page
- Prevents duplicate toy assignments using `Toy.objects.exclude(...)`

### 🗓️ Custom Date Picker
- Integrated [MCDatepicker](https://github.com/Mobius1/MCDatepicker) via CDN
- Initialized in `static/js/cat-detail.js` and styled with `static/css/mcdp.css`

### 🔐 Authentication
- Used Django’s built-in `User` model
- Created login/logout views with session-based auth
- Navbar dynamically renders links based on `user.is_authenticated`
- Logout uses POST method and is styled to match nav links

## 🚀 Final Touches
- All pages styled with `base.css`, custom CSS files for detail/index views
- Feeding form validates and redirects after save
- Many-to-many Toy assignments update dynamically in UI
- Logout button now matches navigation styling

## ✅ Success
You completed a full-stack Django app using class-based views, PostgreSQL, DTL, and Django ORM. You mastered models, templates, URL routing, authentication, and data relationships.

Let’s build even more amazing things, friend. 💪🐾
