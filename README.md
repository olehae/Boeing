# pdsw22_Boeing

## Airline Seat Reservation
This project is part of the course "Programming for Data Scientists: Python" by 
[Gipp Lab](https://gipplab.org/)


## Motivation
The goal of this project is to implement a seat reservation system for an airplane consisting of:
- A relational database for data storage
- A web-based frontend
- A computing backend implemented in Python


## Features
Despite the basic requirements this seat reservation can do things such as:
- Enabling users to sign up and log in via web-interface
- Using Email confirmation codes to sign up new users
- Enabling users to book seats by selecting them from a graphic representation of the planes seat layout


## Code examples
_to do_
```Python
'DIRS': [BASE_DIR / 'templates']
```
Added to TEMPLATE list in settings.py to enable working with a template folder for html files

## Installation
- Make sure that django and sqlite3 is installed to your environment and your environment is activated
- Go to project/boeing/ in your shell and do:
```Shell
python manage.py runserver
```
- Open http://127.0.0.1:8000/ in your browser to access the website
- Use to Ctrl C in the shell to stop the program


## License
Licensed under the Apache License, Version 2.0 (the "License"); you may not use news-please except in compliance with the License. A copy of the License is included in the project, see the file [LICENSE](LICENSE).
