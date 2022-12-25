# How to use

- Make sure that django is installed to your environment and your environment is activated
- Go to project/boeing/ in your shell and do:
```Shell
python manage.py runserver
```
- Open http://127.0.0.1:8000/ in your browser
- Use to Ctrl C in the shell to stop the program

# Login System

```Python
LOGIN_REDIRECT_URL = "home"
LOGOUT_REDIRECT_URL = "home"
```
Added to settings.py to redirect user to the home page after login/logout

```Python
'DIRS': [BASE_DIR / 'templates']
```
Added to TEMPLATE list in settings.py to let django know that there is a templates folder

# Coding Practices (all mandatory)

- During the final presentation, enable the teaching team to test a working prototype, either on
your machine or better running online.
- Structure your source code appropriately into classes according to OOP principles.
- Adhere to the PEP 8 Style Guide and best practice guidelines
- Handle errors properly so the system does not crash.
- Include unit tests for all methods that read in data from external sources or user input and all
methods that manipulate data