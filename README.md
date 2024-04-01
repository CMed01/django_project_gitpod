# Notes

- This codes adds an new installations to the requirements.txt file
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

## Migration
- To migrate model to data structure
    - python3 manage.py makemigrations "name of app" --> this wil create migrations folder
    - python3 manage.py migrate "name of app" --> to run the migration

# META DATA
- Always added after the fields
- Meta class is data about data. This is data that is not a field
- We can use these classes to add functionailty, even calculate fields

# ALLAUTH
- Install app
- Update requirements
- Updated settings.py
    - INSTALLED APPS
    - MIDDLEWARE
- Be sure to migrate when done.
- pip3 show django-allauth
    - this shows the details including the location of the alltuh folder
    - Copy the location and insert it into the following code in the terminal
        - cp -r < template >/allauth/templates/* ./templates/
        - This will create a new folder

# Crispy Forms
- pip3 install django-crispy-forms~=2.0 crispy-bootstrap5~=0.7

# Clouidnary
- pip3 cloudinary~=1.36.0 dj3-cloudinary-storage~=0.0.6 urllib3~=1.26.15
- The only prerequisites to this efficient system are:
    - The Cloudinary package installed in our Django project.
    - Utilize the CloudinaryField in the relevant model.
    - Ensure the CLOUDINARY_URL API key is available in our project environment.

    - It's important to understand that to retrieve the Cloudinary image URL, we use the .url attribute with the post.featured_image field

# HTML validation
- W3C validation tool still used
- Will need to validate by URL
- Note for user appropriate view, will need to login in and inspect the HTML then copy over to validate

# Javascript, CSS, Lighthouse
- No change to validation processers
    - W3C CSS validation
    - JSHINT validation
    - Google lighthouses

# Python
- Continue to use PEP8 code, using the codeinstitute lint checker
- With imports listing
    - Standard library
    - Third-party imports
    - Local imports

- Docstrings """ ..... """ need to be added to class and functions
    - In django model class, also to include models that the foreign key is related to.
        - ":model:'foreign key (auth.User)'"
    - In django function class
        - use the same reference as model class. 
        - Also reference where the data is retrieved from.
    - REMOVE ALL PRINT CODES!!