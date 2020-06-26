# Sanitizer-Dispenser-Login-System
Login email verfication wouldn't work unless you put your Gmail
credentials within the parenthesis at the bottom in the file called 
'setting.py' which can found in the folder named 'sanitizer_dispenser_system'.
```
EMAIL_HOST_USER = '' # your gamil username
EMAIL_HOST_PASSWORD = '' your gmail password
```

---

In order to run the web-app, make sure you are in the directory where 
'manage.py' file resides.
Now open terminal in the directory and type```python manage.py runserver```
<br >
Click the HTTP link it provides when the program runs and it will bring
you to the main page and you can sign up, login and perform other
function available in the web-app at the moment!
<br >
<br >
Thanks for checking out our web-app!

---

**Use this account to login**
username: test1
pass: programming1

**OR**

**Make you own account**

Make sure to follow the steps:
- Add you Gmail credentials at the end of the *settings.py* file
- In your Gmail security allow unsecure apps
- Run ```python manage.py runserver```
