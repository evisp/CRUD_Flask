
##  Install Required Software

###  Install MySQL Server:

```bash
sudo apt update
sudo apt install mysql-server
```

###  Install MySQL Workbench 

This step is optional, but recommended for database management.
You can download and install MySQL Workbench following [this](https://dev.mysql.com/downloads/file/?id=519997) link

### Install Python and Flask

```
sudo apt install python3 python3-pip
pip3 install Flask
```

## Start MySQL Server

```bash
sudo service mysql start
```

## Access MySQL and Create Database

```bash
mysql -u root -p
```

Then
```sql
CREATE DATABASE sakila;
USE sakila;
```

## Download and Import Sakila Database

Download and Import Sakila Sample Database
Visit the MySQL documentation to download the Sakila sample database: MySQL :: [Sakila Sample Database](https://dev.mysql.com/doc/sakila/en/)

After downloading, import the Sakila database using the following command:

```bash
mysql -u root -p sakila < path/to/sakila-schema.sql
mysql -u root -p sakila < path/to/sakila-data.sql
```

## Create Flask Application

### Install Flask-MySQL

```bash
pip install Flask-MySQL
```

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