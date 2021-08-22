### Step Setup:
This is a Guide for setup for this application.

1. Installing Git

    <pre>$ sudo apt install git</pre>
        
2. Install and Setup virtualenv (Also includes setup for workon).

    1. First we need to install python3-pip
       
        <pre>$ sudo apt install python3-pip</pre>
        
    2. Once done, we can now install virtualenv
        
        <pre>$ sudo pip3 install virtualenv</pre>
        
    3. Create Virtual Environment

        <pre>$ python3 -m venv "your virtual env name"</pre>

3. Clone Repository:

    <pre>$ git clone https://github.com/vkscnb/django-groups-for-three-user.git</pre>

4. Create a new Environments for the projects.

    1. Create

        <pre>$ python3 -m venv "your virtual env name"</pre>
    
    2. Activate env

        <pre>$ source "env name"/bin/activate</pre>

5. Postgres database setup
    1. Install Postgres
        <pre>
            $ sudo apt update

            $ sudo apt install postgresql postgresql-contrib
        </pre>  

    2. Create database and user.
        <pre>
            $ sudo su -  postgres

            $ psql

            $ CREATE DATABASE user_db;

            $ CREATE USER test1 WITH PASSWORD 'test';

            $ ALTER ROLE test1 SET client_encoding TO 'utf8';

            $ ALTER ROLE test1 SET default_transaction_isolation TO 'read committed';

            $ ALTER ROLE test1 SET timezone TO 'UTC';

            $ GRANT ALL PRIVILEGES ON DATABASE user_db TO test1;

        </pre>
        
6. Go to the cloned directory ,Location of this is supposed to be "/home/vikas/Desktop".

    1. Go to locations

        <pre>$ cd django-groups-for-three-user</pre>

    2. RUN below commands for install all requirements and db migrations.

        <pre>
            $ pip install -r requirements.txt

            $ python manage.py makemigrations

            $ python manage.py migrate

        </pre>
    
    3. RUN command Create Default grpops
        <pre>
                $ python manage.py create_groups
        </pre>

    3. If all setup are done. Run the Project by-

        <pre>$ python manage.py runserver</pre>

    4. Open in browser-
        <pre>http://127.0.0.1:8000</pre>

    5. For create Super User RUN - 
        <pre>python manage.py createsuperuser --database=user_db</pre>
        
