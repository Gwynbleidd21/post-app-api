# Post app api
Django web app for working with posts via external API.

## Prerequisites
Have docker and docker-compose installed on your machine.
## Installation
Pull from github repo.

Navigate inside project root and execute:
```commandline
docker build .
```
Next we build docker-compose
```commandline
docker-compose build
```
Check linting with flake8
```commandline
docker-compose run --rm app sh -c "python manage.py flake8"
```
## Running and usage
To run the app inside docker use
```commandline
docker-compose up
```
Navigate to url for rest API interface
```commandline
http://127.0.0.1:8000/api/docs/
```
First step is to create a user and then create auth token for the user.

Once token is created, the user needs to be authorized by tokenAuth method via Authorize
```commandline
Token generatedtoken
``` 

API is documented automatically with DRF

