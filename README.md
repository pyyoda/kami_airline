# Kami Airlines

--- A working digital version of the aircraft passenger capacity issue ---

## Requirements

- Python 3.10 or above (`sudo apt-get install python3.10`)
- Poetry (`pip install poetry`)

## Setup and Run Project

1. Clone the Repo

   ```bash
   git pull
   cd
   ```

2. Activate Virtual Enviornment: `poetry shell`

3. Install the project: `poetry install`

4. Populate `.env`:

   Add a `.env` file in the repo root and these variables within that file.
   ( important environment variables to run the project )

   DEBUG=
   SECRET_KEY=
   EMAIL_USER_NAME=''
   EMAIL_PASSWORD=''

5. Run `python manage.py migrate` to trigger migration process of database

6. Run `python manage.py createsuperuser` to create a superuser to access the admin site

7. Run `python manage.py runserver` to run django server

   `Admin Panel`

   - Login into the admin panel using the site: http://127.0.0.1:8000/

   `Note`: You must be logged in before using API
   `Django Rest Framework Api`

   - Use this url to access rest framework api: http://127.0.0.1:8000/airplanes/
   - Use extra functions to get fuel consumption and max minutes to fly or use this url: http://127.0.0.1:8000/airplanes/get-fuel-consumption/

## Test and Generate Coverage Report

1. Run `coverage run --rcfile=.coveragerc manage.py test` to conduct all tests

2. Run `coverage html --rcfile=.coveragerc --directory=coverage_testreport` to generate converage test report

## Set up Linter and Formatter

1. Run `black .` to format code

2. Run `flake8` to lint and see problems
