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
