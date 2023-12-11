# Cloud.io Backend

## About

This is the backend server for the Cloud.io project
The idea was to help faciliate with the provisioning and management of Google cloud compute API services

It was made using **Python 3.11** + **Django** and database is **SQLite**.
Testing is done using **untitest** module.

## Prerequisites

\[Optional\] Install virtual environment:

```bash
$ python -m virtualenv env
```

\[Optional\] Activate virtual environment:

On macOS and Linux:
```bash
$ source env/bin/activate
```

On Windows:
```bash
$ .\env\Scripts\activate
```

Install dependencies:
```bash
$ pip install -r requirements.txt
```

Setup key.json (Get Service Acccount key from Google Cloud Console https://console.cloud.google.com/apis/credentials)

## How to run

### Default

You can run the application from the command line with manage.py.
Go to the root folder of the application.

Run migrations:
```bash
$ python manage.py migrate
```

Run server on port 8000:
```bash
$ python manage.py runserver 8000
```

### Docker

It is also possible to run the blog app using docker:

Build the Docker image:
```bash
$ docker build -t mordax/django-cloudio -f docker/Dockerfile .
```

Run the Docker container:
```bash
$ docker run -d -p 8000:8000 mordax/django-cloudio
```

#### Helper script

It is possible to run all of the above with helper script:

```bash
$ chmod +x scripts/run_docker.sh
$ scripts/run_docker.sh
```

<!-- ### Tests

#### Default
Activate virtual environment:

On macOS and Linux:
```bash
$ source env/bin/activate
```

On Windows:
```bash
$ .\env\Scripts\activate
```

Running tests:
```bash
$ python manage.py test blog
```

#### Docker

It is also possible to run tests using Docker:

Build the Docker image:
```bash
$ docker build -t mordax/django-clouio -f docker/Dockerfile .
```

Run the Docker container:
```bash
$ docker run --rm mordax/django-clouio test blog
``` -->