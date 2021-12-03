# Appointment Scheduler

This repository represents my implementation for the Python Technical Test applied by Tango.

## Installation
Clone this repository

    git clone https://github.com/2Fac3R/Tango.git
    cd Tango

Create or start your virtual environment [venv](https://docs.python.org/3/library/venv.html)

    virtualenv venv 
    source venv/bin/activate

Install requirements. Use the package manager [pip](https://pip.pypa.io/en/stable/)

    pip install -r requirements.txt

Make migrations and migrate

    python3 manage.py makemigrations
    python3 manage.py migrate

Create a superuser

    python3 manage.py createsuperuser

Run the server

    python3 manage.py runserver

You can now access the server at http://127.0.0.1:8000

## Usage

Log in

    http://localhost:8000/admin

You can access to the following routes

    http://localhost:8000/api/users/
    http://localhost:8000/api/groups/
    http://localhost:8000/api/appointments/
    http://localhost:8000/appointments/?id=<user_id>

You can use the Django Rest Framework Browsable API for testing the application.

## Description

* [djangorestframework](https://www.django-rest-framework.org/) It's a powerful and flexible toolkit for building Web APIs.

You can find more details in *requirements.txt* file.

## My thoughts

* I know that the assignment only asks to create 2 endpoints but I'm using DRF so I think it's more comfortable and practical to have User and admin panel for testing the app completely.
* I am using SQLite for testing purposes, having in mind that we're using DRF and Django admin tools.
* I decided to use a single value to represent dates because I think it's more practical and easier to handle.
* According to the following validation requirements:

    all appointments must start and end on the hour or half-hour.
    all appointments are exactly 30-minutes long.

In my opinion, covering the first requirement, all appointments should have the second requirement applied by default unless you split date into "start_date" and "end_date" fields.
* For this assignment User ID is just an incremental integer value, but in more complex systems I would use an UUID hash or something similar.


## TODO

* Validation:

    A User can only have one appointment on a calendar date

I'm trying using UniqueTogetherValidator validator but not fully implemented yet.


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Any feedback is appreciated.