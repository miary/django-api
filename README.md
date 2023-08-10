# Django 4 Rest Framework API with JWT Auth

Simple starter built with Python / Django Rest / Sqlite3 and JWT Auth. The authentication flow is built with [json web tokens](https://jwt.io).

<br />

> Features:

- ✅ `Up-to-date dependencies` 
- ✅ Django 4 / DRF / SQLite3 - a simple, easy to use backend
- ✅ `JWT Authentication` (login, logout, register)
- 🆕 `OAuth` for **Github**
- ✅ Docker, Unitary tests
  
<br />

## ✨ Quick Start in `Docker`

> 👉 Get the code

```bash
$ git clone https://github.com/miary/django-api.git
$ cd django-api
```

> 👉 Start the app in Docker

```bash
$ docker-compose up --build  
```

The API server will start using the PORT `5000`.

<br />

## ✨ How to use the code

> 👉 **Step #1** -  Clone the sources

```bash
$ git clone https://github.com/miary/django-api.git
$ cd django-api
```
<br />

> 👉 **Step #2** - Create a virtual environment

```bash
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv env
$ # .\env\Scripts\activate
```

<br />

> 👉 **Step #3** - Install dependencies using PIP

```bash
$ pip install -r requirements.txt
```

<br />

> 👉 **Step #4** - Create a new `.env` file using sample `env.sample`

The meaning of each variable can be found below: 

- `DEBUG`: if `True` the app runs in develoment mode
  - For production value `False` should be used
- `SECRET_KEY`: used in assets management
- `GITHUB_CLIENT_ID`: For GitHub social login
- `GITHUB_SECRET_KEY`: For GitHub social login

<br />

> 👉 **Step #5** - Start the API server

```bash
$ python manage.py migrate
$ python manage.py runserver
```

The API server will start using the default port `8000`.

<br />

## ✨ Tests

```bash 
$ python manage.py test
```

<br />

## ✨ API

> **Register** - `api/users/signup`

```
POST api/users/signup
Content-Type: application/json

{
    "username":"test",
    "password":"pass", 
    "email":"test@example.com"
}
```

<br />

> **Login** - `api/users/login`

```
POST /api/users/login
Content-Type: application/json

{
    "password":"pass", 
    "email":"test@example.com"
}
```

<br />

> **Logout** - `api/users/logout`

```
POST api/users/logout
Content-Type: application/json
authorization: JWT_TOKEN (returned by Login request)

{
    "token":"JWT_TOKEN"
}
```

<br />

---
**[Django Rest Framework API](https://github.com/miary/django-api)** 
