# BulkIPO
This is the repository of BulkIPO applier application that is built using Django. I built this project to learn and explore web development in Python.

## Step 1: Python Installation
In order to Run this project, you have to install python to your system from the officcial link: [Python Download](https://www.python.org/downloads/)
After download and necessary environment setup, you can proceed to setp 2.

## Step 2: Create a folder for the project
Create a folder inside the root folder with a name of your interest or as follows:

![Root Folder Screenshot](https://github.com/adars124/BulkIPO/blob/main/static/Screenshot%20from%202023-08-24%2019-26-20.png?raw=true)

## Step 3: Install Virtual Environment
You can install virtual environment on your project folder by using the following command in the cli:
```
pip install virtualenv

```

## Step 4: Virtual Environment Setup
To initialize the virtual environment on your project folder, use the following command in the cli:
```
python -m venv <environment_name>

# To start the environment [For Windows]
<environment_name\Scripts\activate

# To start the environment [For macOs and Linux]
cd <environment_name>
source bin/activate

```
![Screenshot after initializing the virtualenv](https://github.com/adars124/BulkIPO/blob/main/static/Screenshot%20from%202023-08-24%2019-31-30.png?raw=true)

## Step 5: Installing requirements
After the virtual environment is all set up, go to the project folder i.e, in this case: ` cd core ` and install the `requirements.txt` file.
```
# For installing requirements
pip install -r requirements.txt

```

## Step 6: Make Migrations
To create a new database file use the following command:
```
python manage.py makemigrations

```

## Step 7: Migrate
After creating the database file, you need to migrate in order to add the tables in the database as follows:
```
python manage.py migrate

```

## Step 8: Runserver
After successful completion of all the above steps, you can run the project by using the command ` python manage.py runserver `.
Then, copy the url from your cli where the server is running and open up a browser and paste it there.

## Step 9: Creating a super user [Optional]
If you want to create a super user to keep track of all the accounts that you add into the database you can use the following command:
```

python manage.py createsuperuser

```
Fill up rest of the details as prompted on your screen.
That's it, now you can easily add multiple MeroShare accounts and apply to newly listed IPOs with a single click.
