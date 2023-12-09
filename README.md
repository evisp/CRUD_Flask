# READ ME - I know you do

This project is a simple web application that showcases several key concepts discussed
at the `Foundations` program at Holberton School. This application gets its data from (a lightversion)
of the [Sakila Sample Database](https://dev.mysql.com/doc/sakila/en/) providing hundreeds of
records of exploring movies and actors, among others. Built using Flask, a lightweight and efficient web framework, and SQLAlchemy, a SQL toolkit for Python, the application demonstrates several functionalities such as

### Key functionalities

* **Trending Movies**: A (random) list of movies is dynamically shown on each visit of the page

* **Search Movies**: A simple search functionality retreives the movies from the database and displays them in a grid like manner 

* Similar operations can be developed for other key entities such as actors. 

### Key technologies
- **Flask** as a web framework which provides tools, libraries, and patterns needed to create *routes* so that
and *url* can be bound to a certain functionality 

- **SQLAlchemy** as a translator between Python code and our MySQL database, so we can store and retreive data
    using Python code instead of SQL queries 

- **MySQL** as a database management system to store and organize information. Our *Sakila* database is created 
    and populated using SQL queries

- **HTML/CSS** for creating the structure and design of our website.

- **Jinja2 (templating engine)** helps us create dynamic web pages. It allows us to mix our Python code with our HTML pages, so we can show different content based on what a user does 

##  Install Required Software

## Install VSCode and Unix-like Command Line

First off, install (or make sure you have installed) [VS Code](https://code.visualstudio.com/). To be able to easily install the required packages in unix-like style, you may want to install as terminal on your VS code
WSL (Windows Subsystem for Linux). To do so, visit [this page](https://learn.microsoft.com/en-us/windows/wsl/install) and follow the instructions provided there.

###  Install MySQL Server 

MySQL server is crucial for our application as it serves as the backend database management system. It stores and retrieves data, providing a structured way for data management. 

Use the commands below to install it and make sure everything is up to date with your Python environment as well. 

```bash
sudo apt update
sudo apt install mysql-server

sudo apt-get install default-libmysqlclient-dev
sudo apt-get install python3-dev
pip install mysqlclient
```

###  Install MySQL Workbench 

This step is optional. 
You can download and install MySQL Workbench following [this](https://dev.mysql.com/downloads/file/?id=519997) link

### Install Flask


Flask is essential for our application as it acts as the web framework. 
It enables us to create dynamic and responsive web pages, handle user requests, and integrate with the backend database. 

```bash
sudo apt install python3 python3-pip
pip3 install Flask
pip install Flask-MySQL
```


### Install Flask-SQLAlchemy and Install SQLAlchemy:

```bash
pip install Flask-SQLAlchemy
pip install SQLAlchemy
```

## Build and Set Up MySQL Server

### Start MySQL Server

```bash
sudo service mysql start
```

### Access MySQL and Create Database

```bash
mysql -u root -p
```

Then
```sql
CREATE DATABASE sakila;
USE sakila;
```

### Download and Import Sakila Database

Download and Import Sakila Sample Database
Visit the MySQL documentation to download the Sakila sample database: MySQL :: [Sakila Sample Database](https://dev.mysql.com/doc/sakila/en/)

After downloading, import the Sakila database using the following command:

```bash
mysql -u root -p sakila < path/to/sakila-schema.sql
mysql -u root -p sakila < path/to/sakila-data.sql
```

Alternatively, you can use a simpler version, by creating just the tables

* [SQL Query to Create Table Actor](https://github.com/evisp/CRUD_Flask/blob/main/sakila-db/insert_actor.sql)
* [SQL Query to Create Table Film](https://github.com/evisp/CRUD_Flask/blob/main/sakila-db/insert_film.sql)
* [SQL Query to Create Table Film_Actor](https://github.com/evisp/CRUD_Flask/blob/main/sakila-db/insert_actor_film.sql)
* [SQL Query to Update Film to include an image url](https://github.com/evisp/CRUD_Flask/blob/main/sakila-db/update_url.sql)

## Create Simple (Hello World) Flask Application

### Create a new directory for your project and navigate into it:

```bash
mkdir flask-crud-app
cd flask-crud-app
```
### Create init app file

Create a file named `app.py` for your Flask application:

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

```

### Create HTML Templates

Create a folder named `templates` in your project directory. Inside this folder, create an HTML file named `index.html` 

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask CRUD App</title>
</head>
<body>
    <h1>Hello, Flask CRUD App!</h1>
</body>
</html>

```

### Run Your Flask App

```python
python app.py
```
