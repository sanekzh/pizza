Requirements PIZZA:
=============
1. Python 3.6
2. virtualenv
3. MySQL [[reference]](https://dev.mysql.com/downloads/installer/)

          
How to install:
===============

1. Clone project:
    ```bash
            $ git clone 
    ```       

2. Create and activate virtualenv (python 3.6)
3. Create databases in MySQL client
4. Install requirements:
    ```bash
        $ pip install -r requirements.txt
    ```
5. Apply all migrations to all databases: 
    ```bash
        $ python manage.py migrate
    ```
6. Create super user

How to run:
===========
1. PIZZA
    ```bash
            $ python manage.py runserver 
    ```
