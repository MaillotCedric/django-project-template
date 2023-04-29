# django-project-template

Template for Django projects

The template is based on Django framework and allows you to rapidly create a RESTfull API with django REST framework

## Setup repository

a. Choose a new repository name

b. Use it to rename the current cloned repository

c. Delete the current `.git` folder (the folder might be hidden)

d. Update README.md

e. Run the following command in the terminal of the repository

  ```
  git init
  git add .
  git commit -m "Init repository"
  ```

*You are now ready to install the project :)*

## Installation

- Install a virtual environment :
  
  - Windows :
    
    `py -m venv .env`
    
  - Linux or Mac OS :
    
    `python3 -m venv .env` or `python -m venv .env`
    
- Activate the virtual environment :
  
  - Windows :
    
    `.env\Scripts\activate`
    
  - Linux or Mac OS :
    
    `source .env/bin/activate`
    
- Install packages (Django, ...) :
  
  `pip install -r requirements.txt`

- Hide the key to the castle :

  - Create the safe :
  
     Inside `project` folder, create a file called `.env`
    
  - Generate the key [(*source*)](https://codinggear.blog/django-generate-secret-key/?utm_content=cmp-true/) :
  
     a. Run the following command in the terminal of your Django project
    
     . Windows :
    
      `py manage.py shell`
     
     . Linux or Mac OS :
     
      `python3 manage.py shell` or `python manage.py shell`
     
     b. Import the key generator function
    
     Run the following command and hit `Enter` :
    
      `from django.core.management.utils import get_random_secret_key`
      
     c. Generate a random key
     
     On the next line we can now use the function to generate the secret key
     
      `print(get_random_secret_key())`
      
     
   - Hide the key
   
     Copy the generated key
     
     In the `.env` file, declare a `SECRET_KEY` variable as follows
     
      `SECRET_KEY=<generated key>`
      
   *The castle is well-protected now :)*

---

### If you using a PostgreSQL database

- Install the PostgreSQL database connection package
  
  - Windows :
    
    `pip install psycopg2`
    
  - Linux or Mac OS :
    
    `pip install psycopg2-binary`
    
- Create database :
  
  - Database settings :
    
    - Name : ``<database's name>``
    - User : ``<database's user's name> (default : postgres)``
    - Password : ``<database's password>``
  
- Update `project/settings.py` [(*source*)](https://codinggear.blog/django-environment-variables/) :
  
  ```python
  DATABASES = {
      "default": {
          "ENGINE": "django.db.backends.postgresql_psycopg2",
          "NAME": os.environ.get("DB_NAME"),
          "USER": os.environ.get("DB_USER_NAME"),
          "PASSWORD": os.environ.get("DB_PASSWORD"),
          "HOST": "127.0.0.1",
          "PORT": "5432",
      }
  }
  ```
  
- Update `project/.env` :
  
  ```
  DB_NAME=<database's name>
  DB_USER_NAME=<database's user's name> (default : postgres)
  DB_PASSWORD=<database's password>
  ```

---

- Make the first migrations :
  
  - Windows :
    
    `py manage.py makemigrations`
    
    `py manage.py migrate`
    
  - Linux or Mac OS :
    
    `python3 manage.py migrate` or `python manage.py migrate`
    
    `python3 manage.py makemigrations` or `python manage.py makemigrations`
    
    `python3 manage.py migrate` or `python manage.py migrate`
    
- Create datasets :

  - Windows :

    `py manage.py init_local_dev`

  - Linux or Mac OS :

    `python3 manage.py init_local_dev` or `python manage.py init_local_dev`

- Update `.env/lib/python3.10/site-packages/django/contrib/auth/base_user.py` :

  ```python
  from django.db import transaction

  class AbstractBaseUser(models.Model):
    password = models.CharField(_("password"), max_length=128)
    last_login = models.DateTimeField(_("last login"), blank=True, null=True)
    #...
    @transaction.atomic
    def deactivate(self):
        if self.is_active is False:
            return
        
        self.is_active = False
        self.save()

    @transaction.atomic
    def activate(self):
        if self.is_active is True:
            return
        
        self.is_active = True
        self.save()
  ```

---

## API REST

| URI                                               | Authorization    | Method | Data      | Description                  |
| ------------------------------------------------- | ---------------- | ------ | --------- | ---------------------------- |
|                /api/users/                        | No Auth          | GET    | None      | Get users list               |
|                /api/users/{{id_user}}/            | No Auth          | GET    | None      | Get user instance            |
|                /api/users/{{id_user}}/            | Basic Auth       | PATCH  | `[email]` | Update user's instance email |
|                /api/users/{{id_user}}/deactivate/ | Basic Auth       | PATCH  | None      | Deactivate user instance     |
|                /api/users/{{id_user}}/activate/   | Basic Auth       | PATCH  | None      | Activate user instance       |

---
