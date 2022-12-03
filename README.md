# CS130-Intervtopia
Intervtopia: A Web Application for Mock Interviews between Peers

## Team members:
Wenhe Zhang, Haofan Lu, Reza Rezvani, Keli Huang, Mehrab Beikzadeh, and Yadi Cao

## Automated Test
We have 2 catogories of auto tests: 1) the django and 2) the general unit tests supported by python's unittest module.
Please refer to this [Tutorial](https://docs.djangoproject.com/en/4.1/intro/tutorial05/) on how to use the django's auto test systems. There are some example test cases.
The django tests are in the `test/django_tests/`. The general tests are in `test/`. All test file names must start with `test*` in order to be captured.
To run the auto test use the following command in the `repo_root/intervtopia/` directory:
```
python run_tests.py
```

### Instant web services
We generate the meeting rooms/workspaces using existing online service providers for easier integration. The unique workspace id generation is done by hashcode of the particitants. These services are then wrapped into a bigger Facede for easier use by users.
- Online IDE, supported by [jitsi meet](https://meet.jit.si/)
- Online Video Conference room, supported by [Codeshare](https://codeshare.io/)

# Backend
Run following code in the terminal
   ```
   pip3 install -r requirements.txt
   python3 manage.py makemigrations
   python3 manage.py migrate
   python3 manage.py runserver
   ```

   To see the site: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

# Frontend

- Install NodeJs from [NodeJs Official Page](https://nodejs.org/en/)
- Open a second Terminal, go to the "frontend" folder
- Run in terminal: `npm install`
- Then: `npm start`
- Navigate to `http://localhost:3000`, the frontend webpage is shown here.
