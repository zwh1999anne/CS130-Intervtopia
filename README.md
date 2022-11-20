# CS130-Intervtopia
Intervtopia: A Web Application for Mock Interviews between Peers

## Team members:
Wenhe Zhang, Haofan Lu, Reza Rezvani, Keli Huang, Mehrab Beikzadeh, and Yadi Cao

## Notes for Devs:
### Requirements:
- django
- yapf (code formatter; formatting file provided in `repo_root/intervtopia/.style.yapf`). Auto-formatting must be done through `yapf -ir intervtopia` (in repo root) or `yapf -ir .` (in `intervtopia`) before commit.

### Git Ignore:
If you see pycache files in `git status`, make sure removing them before commit. This should not happen after a commit where `**/__pycache__/*` is included in the `.gitigore`; However, they may be re-commited if you merge or rebase some older commits.


## Automated Test
We have 2 catogories of auto tests: 1) the django and 2) the general unit tests supported by python's unittest module.
Please refer to this [Tutorial](https://docs.djangoproject.com/en/4.1/intro/tutorial05/) on how to use the django's auto test systems. There are some example test cases.
The django tests are in the `test/django_tests/`. The general tests are in `test/`. All test file names must start with `test*` in order to be captured.
To run the auto test use the following command in the `repo_root/intervtopia/` directory:
```
python run_tests.py
```

## Evaluation App
evaluation is the application handling the evaluation forms


## Database

SQLite database is used by django by default. It hosts two models for this application: `Question` and `Choice`.

With a superuser account, you can view and manage the database in GUI. To create a superuser account, run following command: 
```
python manage.py createsuperuser
```
Please refer to this [Tutorial](https://docs.djangoproject.com/en/4.1/intro/tutorial02/) for basic usage about the database.
Please dig into this [Documentation](https://docs.djangoproject.com/en/4.1/ref/databases/#sqlite-notes) for more information.


## User system


## External libraries and services

### Instant web services
We generate the meeting rooms/workspaces using existing online service providers for easier integration. The unique workspace id generation is done by hashcode of the particitants. These services are then wrapped into a bigger Facede for easier use by users.
- Online IDE, supported by [jitsi meet](https://meet.jit.si/)
- Online Video Conference room, supported by [Codeshare](https://codeshare.io/)

# Installation
   ```
   pip3 install -r requirements.txt
   python3 manage.py makemigrations
   python3 manage.py migrate
   python3 manage.py test # Run the test
   python3 manage.py createsuperuser # Create a superuser
   python3 manage.py runserver
   ```

   To see the admin site: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)