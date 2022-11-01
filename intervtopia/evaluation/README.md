# Evaluation App
evaluation is the application handling the evaluation forms

## Automated Test
The test code is written in the `tests.py` file.
To run the auto test use the following command in top directory:
```
python managy.py test evaluation
```
Please refer to this [Tutorial](https://docs.djangoproject.com/en/4.1/intro/tutorial05/) on how to use the django's auto test systems. There are some example test cases.

# Database

SQLite database is used by django by default. It hosts two models for this application: `Question` and `Choice`.

With a superuser account, you can view and manage the database in GUI. To create a superuser account, run following command: 
```
python manage.py createsuperuser
```
Please refer to this [Tutorial](https://docs.djangoproject.com/en/4.1/intro/tutorial02/) for basic usage about the database.
Please dig into this [Documentation](https://docs.djangoproject.com/en/4.1/ref/databases/#sqlite-notes) for more information.