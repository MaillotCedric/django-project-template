# django-project-template

Template for Django project

The template is based on Django framework and allows you to rapidly create a RESTfull API with django REST framework

## Installation

- Install a virtual environment :
  
  - Windows :
    
    `py -m venv .env`
    
  - Linux or Mac OS :
    
    `python3 -m venv .env` ou `python -m venv .env`
    
- Activate the virtual environment :
  
  - Windows :
    
    `.env\Scripts\activate`
    
  - Linux or Mac OS :
    
    `source .env/bin/activate`
    
- Install packages (Django, ...) :
  
  `pip install -r requirements.txt`
  

---

### If you using a PostgreSQL database

- Install the PostgreSQL database connection package
  
  - Windows :
    
    `pip install psycopg2`
    
  - Linux or Mac OS :
    
    `pip install psycopg2-binary`
    
- Create database :
  
  - Database settings :
    
    - Name : ``<database name>``
    - User : ``<user name> (default : postgres)``
    - Password : ``<database password>``
- Update `project/settings.py` :
  
  ```python
  DATABASES = {
      "default": {
          "ENGINE": "django.db.backends.postgresql_psycopg2",
          "NAME": "<database name>",
          "USER": "<user name> (default : postgres)",
          "PASSWORD": "<database password>",
          "HOST": "127.0.0.1",
          "PORT": "5432",
      }
  }
  ```
  

---

- Make the first migrations :
  
  - Windows :
    
    `py manage.py makemigrations`
    
    `py manage.py migrate`
    
  - Linux or Mac OS :
    
    `python3 manage.py migrate` ou `python manage.py migrate`
    
    `python3 manage.py makemigrations` ou `python manage.py makemigrations`
    
    `python3 manage.py migrate` ou `python manage.py migrate`
