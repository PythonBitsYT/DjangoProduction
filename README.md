# README #
#! TODO-Boilerplate: Fix this name
Below documentation takes you over a step-by-step guide to setup djangoprod microservice on your machine

## Requirements

Python version [3.9.9](https://www.python.org/downloads/release/python-399/) is required for this setup. 
It is strongly recommended that you are using the same version. As, not using the same python version coul result in inconsistent results and dependency breaks on higher environments.


## Contribution guidelines ##

* All code must have proper unit and behavior test case changes. Any pull request without proper test cases will be rejected


### Who do I talk to? ###

* rishabhojha11@gmail.com
 

### Requirements

* Python - 3.9.9


### Setup

The first thing to do is to clone the repository:

```bash
#! TODO: Change this
$ git clone https://github.com/PythonBitsYT/DjangoProduction.git
$ cd DjangoProduction
```

Use python [3.9.9](https://www.python.org/downloads/release/python-399/) to create a new environment and activate it

```bash
$ python3 -m venv env

# Once the environment is setup activate it
$ source env/bin/activate
```

Then install python dependencies (use the package manager [pip](https://pip.pypa.io/en/stable/)):

```bash
(env)$ pip install -r requirements_<env>.txt
```
#! TODO-Boilerplate: Fix this name
Create a `.env` file at the same level as djangoprod, copy all the environment
variables from `.env.example` or `.env.test` and update the values


Create `logs` folder inside at the same level as djangoprod


Run migrations & server:
```bash
(env)$ python manage.py migrate
(env)$ python manage.py runserver
```


Now the server is up and running on `http://127.0.0.1:8000/`.
