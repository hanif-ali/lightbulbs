# Lightbulbs
> A Social Networking platform for sharing ideas

[![for-cs114](https://img.shields.io/badge/for-CS%20114-blue)](http://www.nust.edu.pk/INSTITUTIONS/Schools/SEECS/ap/ug/BSE-2018/Pages/Course-Curriculum.aspx)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-v3-blue)](https://www.djangoproject.org/)
[![built-with-love](https://img.shields.io/badge/Built%20with-%E2%9D%A4%EF%B8%8F%20for%20%3C%2F%3E-red)]()
[![dependencies](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen)]()
[![license](https://img.shields.io/badge/license-MIT-%23373737)]()

Lightbulbs is an idea sharing platform that brings like minded people together to share and discuss ideas.

# Installation Steps

Follow the steps below to get a local copy of the project up and running on your machine.

## Windows
------------
### 1. Cloning
```
git clone https://github.com/hanif-ali/lightbulbs.git
```
Alternatively you can download the ZIP from the top of this page.

### 2.Creating Virtual Environment
`cd` into the directory and create a Virtual Environment by running
```
py -m venv env
```

### 3. Activating the Virtual Environment
To activate the virtual environment run
`env\Scripts\activate.bat` in Command Prompt or `env\Scripts\activate` in Windows Powershell.

### 4. Installing Dependencies
To install the dependencies, run
```
pip install -r requirements.txt
```

### 5. Running Database Migrations
Run `cd lightbulbs` to move into the inner lightbulbs directory and run
```
python manage.py makemigrations
```
```
python manage.py migrate
```

### 6. Load Root User Fixture
To load the Super User's fixture, run
```
python manage.py loaddata UserFixture.json
```

### 7. Start Up The Server
Run the localhost using
```
python manage.py runserver
```

## Linux
----------
The steps are same as above. Except, you may need to replace `py` with `python3` while creating the Virtual Environments. If your Python 3 executable is pointed to by `python`, run that. Moreover, the virtual environment is activated by running `env/bin/activate`. 

# Contributing
If you want to contribute any feature to the application, fork this repository and Submit a pull request once you think it is ready to merge.
Create issues to report bugs or suggest any form of changes.
All forms of contribution are highly welcomed.
