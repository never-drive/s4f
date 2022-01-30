# Django

Getting started -> [intro](https://docs.djangoproject.com/en/4.0/intro/)

## Tutorial

Throughout this tutorial, we’ll walk you through the creation of a basic **poll application**.

### Part 1

* Creating a project
    * `python -m django --version`
    * `django-admin startproject mysite`
* The development server
    * `python manage.py runserver`
* Creating the Polls app
    * `python manage.py startapp polls`
* Write your first view

### Part 2

* Database setup
    * `python manage.py migrate`
* Creating and activating models
    * `python manage.py makemigrations polls`
    * `python manage.py sqlmigrate polls 0001`
    * `python manage.py migrate`
* Playing with the API
    * `python manage.py shell`
* Introducing the Django Admin
    * `python manage.py createsuperuser`

### Part 3

* Writing more views that actually do something
* Raising a 404 error
* Use the template system

### Part 4

* Write a minimal form
* Use generic views: Less code is better

### Part 5

* Writing our first test
    * `python manage.py test polls`
* Test a view

### Part 6

* Customize the app’s look and feel
* Customize the admin form
* Publish a REST API -> [Getting Started with Tastypie](https://django-tastypie.readthedocs.io/en/latest/tutorial.html)
    * `pipenv install django-tastypie`
    * `python manage.py startapp api`
* JSON Formatter -> [Chrome Extension](https://chrome.google.com/webstore/detail/json-formatter/bcjindcccaagfpapjjmafapmmgkkhgoa)
* Home page added

### Part 7

Follow the instructions below to deploy the app to Heroku:

* Intro -> [Sign up](https://signup.heroku.com/)
* Set up -> [Install CLI](https://devcenter.heroku.com/categories/command-line)
    * `heroku login`
* Prepare the app -> skip it! (no `git clone` needed)
* Installation of dependencies (gunicorn, psycopg2, django-heroku, whitenoise)
    * `pipenv shell`  
    * `pipenv install`    
* Run the app locally
    * `python manage.py collectstatic`
    * `heroku local -f Procfile.windows`
* Push local changes
    * `git init`
    * `git add .`
    * `git commit -m "First commit"`
* Deploy the app
    * `heroku create`
    * `git push heroku master`
    * `heroku ps:scale web=1`
    * `heroku open`
* Define config vars
    * `heroku config:set TIMES=2`
* Provision a database (preparation of remote data)
    * `heroku run python manage.py makemigrations`
    * `heroku run python manage.py migrate`
    * `heroku run python manage.py createsuperuser`

Source: [Getting Started on Heroku with Python](https://devcenter.heroku.com/articles/getting-started-with-python)
