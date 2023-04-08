# django-project-template

Template for Django projects

The template is based on Django framework and allows you to rapidly create a RESTfull API with django REST framework

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
    
    `python3 manage.py migrate` or `python manage.py migrate`
    
    `python3 manage.py makemigrations` or `python manage.py makemigrations`
    
    `python3 manage.py migrate` or `python manage.py migrate`
