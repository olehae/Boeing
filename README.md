# Python for Data Science - Boeing

## Airline Seat Reservation
This project is part of the course "Programming for Data Scientists: Python" by 
[Gipp Lab](https://gipplab.org/) at the University of Göttingen.


## Motivation
The goal of this project is to implement a seat reservation system for an airplane consisting of:
- A relational database for data storage
- A web-based frontend
- A computing backend implemented in Python


## Features
Despite the basic requirements given in the 
[Project Description](project/project_description/Project_Description_ASR.pdf), 
this seat reservation can do things such as:
- Enabling users to sign up and log in via web-interface
- Using Email confirmation codes to sign up new users
- Enabling users to book seats by selecting them from a graphic representation of the planes seat layout


## Code examples
```Python
'DIRS': [BASE_DIR / 'templates']
```
Added to TEMPLATE list in settings.py to enable working with a template folder for html files

```Python
user = cursor.execute("SELECT * FROM user WHERE username = ? AND password = ?", 
                     (request.POST['username'], 
                     sha512(str(request.POST["password"]).encode('utf-8')).hexdigest())).fetchall()
request.session["userid"] = user[0][0]
request.session["name"] = user[0][1]
request.session["username"] = user[0][2]
request.session["email"] = user[0][3]
request.session["superuser"] = user[0][4]
request.session.set_expiry(0)  # Session expires when the browser is closed
```
Log in user by comparing given username and sha512 sum of given password to the user table in the database.
Important Information about the currently logged-in user is stored in Django´s built-in session framework.
The current session ends if either the user logs out via log out button or the browser is closed.

```Python
output_str = ""
for elem in seats:
    if elem[1] == "A":
        output_str += f"\n{elem[0]}\t"
    if elem[1] == middle:
        output_str += " | | "
    if elem[2]:
        output_str += " X "
    else:
        output_str += f" {elem[1]} "
```
Formatting the seats into a string that is displayed on the overview page. In this example every elem is a list with 
the attributes of an individual seat. elem[0] represents the row, elem[1] is the letter and elem[3] is the booking status.

## Installation
- Make sure that all the [requirements](project/boeing/requirements.txt) are installed to your environment and your environment is activated
- Go to project/boeing/ in your shell and do:
```Shell
python manage.py runserver
```
- Open http://127.0.0.1:8000/ in your browser to access the website
- Use to Ctrl C in the shell to stop the program

## Contributors
| Name                                          | Contributions                                                                      |
|-----------------------------------------------|------------------------------------------------------------------------------------|
| [Niklas](https://github.com/Niklas257)        | <li>display seats <li>css <li>reserve / cancel seats                               |
| [Ole](https://github.com/olehae)              | <li>input data <li>login <li>reserve / cancel seats <li>admin plots <li>deployment |
| [Tom](https://github.com/tomschewski)         | <li>login / logout <li>account db <li>email system                                 |
| [Hermann Josef](https://github.com/hjhueffer) | <li>help page <li>orientation buttons                                              |                                            |
| [Nathan](https://github.com/NathanSoeding)    | <li>admin stats <li>text file overview                                             |

## Deployment
You can visit the deployed version of this project at:

### https://olehae.pythonanywhere.com

## License
Licensed under the Apache License, Version 2.0 (the "License"); you may not use news-please except in compliance 
with the License. A copy of the License is included in the project, see the file [LICENSE](LICENSE).
