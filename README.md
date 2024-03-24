# Notes

- pip3 freeze --local > requirements.txt

## Database

pip3 install dj-database-url~=0.5 psycopg2~=2.9

- dj-databse-url 
    - This is a python package that connects Django to a databse using a URL
- psycopg2
    - This is a driver for interacting with the PostgreSQL database using Python

## Field Types

- [User types](https://docs.djangoproject.com/en/5.0/ref/contrib/auth/), check out the model fields options that Django provides.
- [Field Types](https://docs.djangoproject.com/en/4.2/ref/models/fields/#model-field-types), check out the Django documentation here.

## Static Files Setup
- WHitenoise is an application that can be used to deploy static files on Heroku
    - pip3 install whitenoise~=5.3.0

- Note: The WhiteNoise middleware must be placed directly after the Django SecurityMiddleware.
    - 'whitenoise.middleware.WhiteNoiseMiddleware',

- Once installed
    - python3 manage.py collectstatic