# Base python package
FROM python:3.8-slim-buster

# Working directory
WORKDIR /app

# Copy the dependencies
COPY requirements.txt /app/

# Install the dependencies
RUN pip3 install -r requirements.txt

# Copy the files
COPY . .

RUN python3 manage.py makemigrations
RUN python3 manage.py migrate

RUN python3 manage.py init_local_dev

EXPOSE 8000

# Executable commands
CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000"]
