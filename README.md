# Purchase Tracker Backend

This is the Django REST Framework backend for the Purchase Tracker application. It provides API endpoints for user authentication and managing purchased items.

## Features

- User registration and authentication (Token-based)
- Create, read, update, and delete purchased items
- Calculate cost per day since purchase
- Image upload support for items
- CORS-enabled for frontend integration

## Requirements

- Python 3.10+
- Django 4.x
- Django REST Framework
- dj-rest-auth
- djoser
- Pillow (for image handling)
- django-cors-headers

## Getting Started

### Clone the repository

```bash
git clone https://github.com/charlespalmerbf/purchase-tracker-backend.git
cd purchase-tracker-backend
```

### Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run migrations

```bash
python manage.py migrate
```

### Create a superuser (optional)

```bash
python manage.py createsuperuser
```

### Start the development server

```bash
python manage.py runserver
```

### API Endpoints

| Endpoint                  | Method | Description                 |
|---------------------------|--------|-----------------------------|
| /auth/login/              | POST   | Login and receive token     |
| /auth/logout/             | POST   | Logout and revoke token     |
| /auth/users/              | POST   | Register new user           |
| /items/                   | GET    | List all user items         |
| /items/                   | POST   | Create a new item           |
| /items/{id}/              | PUT    | Update an existing item     |
| /items/{id}/              | DELETE | Delete an item              |

## Environment Variables

Create a `.env` file and add the following if needed:

```env
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

## Media Files

Uploaded item images are stored in the `media/items/` directory. Ensure your `MEDIA_URL` and `MEDIA_ROOT` settings are configured in `settings.py`.
