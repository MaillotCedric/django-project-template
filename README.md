# Project template : Django

Template for Django projects.

The template is based on Django framework and allows you to rapidly create a RESTfull API with django REST framework.

## Setting up the repository

- Choose a new repository name

- Use it to rename the current cloned repository

- Delete the current `.git` folder (the folder might be hidden)

- Update `README.md`

- Run the following command in the terminal of the repository :
  
  ```git
  git init
  git add .
  git commit -m "<commit message>"
  ```

*You are now ready to install the project. :)*

## Installation

- Install a virtual environment
  
  ```powershell
  <Python command> -m venv .env
  ```

- Activate the virtual environment
  
  - Windows
    
    ```powershell
    .env\Scripts\activate
    ```
  
  - Linux
    
    ```powershell
    source .env/bin/activate
    ```

- Install packages
  
  ```powershell
  pip install -r requirements.txt
  ```

- Hide the key to the castle
  
  - Create the safe
    
    Inside `project` folder, create a file called `.env`.
  
  - Generate the key
    
    We gonna generate the key through the Django shell interface.
    
    To launch the shell interface, run the following command in the terminal of your Django project :
    
    ```powershell
    <Python command> manage.py shell
    ```
    
    - Import the key generator function
      
      Run the following command and hit `Enter` :
      
      ```python
      from django.core.management.utils import get_random_secret_key
      ```
    
    - Generate a random key
      
      On the next line we can now use the function to generate the secret key.
      
      ```python
      print(get_random_secret_key())
      ```
    
    - Hide the key
      
      Copy the generated key and exit the shell interface using the following command :
      
      ```python
      exit()
      ```
      
      In the `.env` file, declare a `SECRET_KEY` variable as follows :
      
      ```python
      SECRET_KEY=<generated key>
      ```
      
      *The castle is well-protected now. :)*

- Setting up the database
  
  - Install the PostgreSQL database connection package
    
    - Windows
      
      ```powershell
      pip install psycopg2
      ```
    
    - Linux
      
      ```powershell
      pip install psycopg2-binary
      ```
  
  - Create the database through pgAdmin
  
  - Update `project/settings.py`
    
    ```python
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "NAME": os.environ.get("DB_NAME"),
            "USER": os.environ.get("DB_USER"),
            "PASSWORD": os.environ.get("DB_PASSWORD"),
            "HOST": "127.0.0.1",
            "PORT": "5432",
        }
    }
    ```
  
  - Update `project/.env`
    
    ```python
    DB_NAME=<database name>
    DB_USER=<database user>
    DB_PASSWORD=<database password>
    ```

- Make the first migrations
  
  ```powershell
  <Python command> manage.py makemigrations
  <Python command> manage.py migrate
  ```

- Populate database
  
  ```powershell
  <Python command> manage.py init_local_dev
  ```
  
  When populating the database, a superuser is created.
  
  Superuser credentials :
  
  - Username : admin
  
  - Password : admin

- Update `base_user.py`
  
  ```python
  # Windows : .env/Lib/site-packages/django/contrib/auth/base_user.py
  # Linux : .env/lib/python<Python version>/site-packages/django/contrib/auth/base_user.py
  
  from django.db import transaction
  
  class AbstractBaseUser(models.Model):
    password = models.CharField(_("password"), max_length=128)
    last_login = models.DateTimeField(_("last login"), blank=True, null=True)
    #...
    @transaction.atomic
    def deactivate(self):
        if self.is_active is True:
            self.is_active = False
            self.save()
  
    @transaction.atomic
    def activate(self):
        if self.is_active is False:
            self.is_active = True
            self.save()
  ```

## API REST

| URI                                | Authorization | Method | Data                                   | Description                  |
| ---------------------------------- | ------------- | ------ | -------------------------------------- | ---------------------------- |
| /api/users/                        | No Auth       | GET    | None                                   | List of users                |
| /api/users/{{id_user}}/            | No Auth       | GET    | None                                   | User instance                |
| /api/users/{{id_user}}/            | Bearer Token  | PATCH  | email: `string`                        | Update user's instance email |
| /api/users/{{id_user}}/activate/   | Bearer Token  | PATCH  | None                                   | Activate user instance       |
| /api/users/{{id_user}}/deactivate/ | Bearer Token  | PATCH  | None                                   | Deactivate user instance     |
| /api/predict/                      | No Auth       | GET    | None                                   | Dummy price prediction       |
| /api/token/                        | No Auth       | POST   | username: `string`, password: `string` | Access and refresh tokens    |
| /api/token/refresh/                | No Auth       | POST   | refresh: `string`                      | New access token             |

Tokens lifetime :

- access token : 1 day
- refresh token : 15 minutes

## Run server

``` powershell
<Python command> manage.py runserver
```
## Deployment

When deploying your application you’ll need to run :

``` powershell
<Python command> manage.py collectstatic
```

This command will put all your static files into `STATIC_ROOT` (constant found in `./project/settings.py`).

*<ins>N.B.</ins> : If you’re running on Heroku, then this is done automatically for you.*

## Quick installation

For a quick and easy installation we using **Docker**, so make sure you have Docker installed.

> [How to install and use Docker](https://docs.docker.com/)

### Containerize the application

Run the following command in the terminal of the repository :

```bash
docker compose up -d --build
```

### Access the application

Now that we have our container up and running, we can easily access the application by opening our favorite browser to http://localhost:8000

## Update the application

Since our application is containerized, when you update the application, you are gonna have to rebuild the Docker container to see the effective updates.

You can rebuild the container by running the following commands in the terminal of the repository :

```bash
# rebuild the container
docker compose up -d --build
# remove old images
docker image prune
```

## Stop the container

You can stop the container by running the following command in the terminal of the repository :

```bash
docker compose stop
```

> When stopping the container, the application is not accessible anymore.
>
> To access the application again, you are gonna have to restart the container.

You can restart the container by running the following command in the terminal of the repository :

```bash
docker compose start
```
## Share the application

To share the application, we have to use a Docker registry.

The default registry is Docker Hub.

> [More information on how to share an app](https://docs.docker.com/get-started/04_sharing_app/)

### Push on Hub

Run the following commands in the terminal of the repository :

```bash
docker build -t YOUR-USER-NAME/django-project-template-app .
# if you are not logged in
docker login
docker push YOUR-USER-NAME/django-project-template-app
```

### Update on Hub

Run the following commands in the terminal of the repository :

```bash
docker build -t YOUR-USER-NAME/django-project-template-app .
docker image prune
# if you are not logged in
docker login
docker push YOUR-USER-NAME/django-project-template-app
```
