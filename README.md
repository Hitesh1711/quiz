# Introduction

Quiz game for web made in Django
Written by Hitesh Bhatewada,Purvansh Parmar, Sandhya Tiwari
Under The GNU

### Main features

* Separated dev and production settings

* Example app with custom user model

* Bootstrap static files included

* User registration and logging in as demo

* Requirements files for easy deployments

* SQLite by default

### User Journey
* land on page
* select a category
* start quiz:
  * 5 Questions appear on once.
  * answer each question.
  * Click on answer if correct then green ✌️✌️if wrong then red😡😡.

Categories:
* Computer
* Aptitude
* Programming
* Reasoning

### Existing virtualenv

If your project is already in an existing python3 virtualenv first install django by running

    $ pip install -r requirements.txt
    
And then run the project with :

    $ python manage.py runserver
      
### No virtualenv

This assumes that `python3` is linked to valid installation of python 3 and that `pip` is installed and `pip3`is valid
for installing python 3 packages.

Installing inside virtualenv is recommended, however you can start your project without virtualenv too.

If you don't have django installed for python 3 then run:

    $ pip3 install -r requirements.txt
    
And then:

    $ python manage.py runserver
    
###Images

![image-name](https://i.ibb.co/qDgThBx/Screenshot-272.png)
![image-name](https://i.ibb.co/TcyrstB/Screenshot-271.png)
![image-name](https://i.ibb.co/X4VFYp6/Screenshot-273.png)
