# Basic-Flask-CRUD

## Steps to start projects app
To start this project, create a virtual environment an activate it

```bash
python3.10 -m venv venv
source venv/bin/activate
```

## install required packages

```bash
pip install -r requirements.txt
```

## DB Setup
rename env.example file to .env and update your Database credentials there

## Run the Migrations

flask db migrate
flask db upgrade

## Finally start projects app

```bash
flask --app app run
```