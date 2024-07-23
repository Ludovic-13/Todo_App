from os import environ

DB_HOST=environ.get("DB_HOST")
DB_PORT=environ.get("DB_PORT")
DB=environ.get("DB")
SECRET_KEY=environ.get("SECRET_KEY")
API_KEY=environ.get("API_KEY")