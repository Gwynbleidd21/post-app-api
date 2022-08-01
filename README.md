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
## Running
To run the app inside docker use
```commandline
docker-compose up
```
