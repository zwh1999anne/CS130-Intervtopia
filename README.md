# CS130-Intervtopia
Intervtopia: A Web Application for Mock Interviews between Peers

## Team members:
Wenhe Zhang, Haofan Lu, Reza Rezvani, Keli Huang, Mehrab Beikzadeh, and Yadi Cao

# Evaluation App
evaluation is the application handling the evaluation forms

## Automated Test
We have 2 catogories of auto tests: 1) the django and 2) the general unit tests supported by python's unittest module.
Please refer to this [Tutorial](https://docs.djangoproject.com/en/4.1/intro/tutorial05/) on how to use the django's auto test systems. There are some example test cases.
The django tests are in the `test/django_tests/`. The general tests are in `test/`. All test file names must start with `test*` in order to be captured.
To run the auto test use the following command in the `repo_root/intervtopia/` directory:
```
python run_tests.py
```

# Database

SQLite database is used by django by default. It hosts two models for this application: `Question` and `Choice`.

With a superuser account, you can view and manage the database in GUI. To create a superuser account, run following command: 
```
python manage.py createsuperuser
```
Please refer to this [Tutorial](https://docs.djangoproject.com/en/4.1/intro/tutorial02/) for basic usage about the database.
Please dig into this [Documentation](https://docs.djangoproject.com/en/4.1/ref/databases/#sqlite-notes) for more information.
