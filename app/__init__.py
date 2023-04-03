from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# import upload_file 
# from auth import key, time_line
# from flask_wtf.csrf import CSRFProtect
from flask_caching import Cache

app = Flask(__name__)

#  UPLADO FILES CONFIGRETION 
# app.config['UPLOAD_FILE'] = upload_file
# app.config['FILE_TYPE'] = file_type
# app.config['FILE_SIZE'] = file_size
# app.config['FILES_PATH'] = files_path
# app.config['GET_URL'] = get_url

# APP  CONFIG
app.config['SECRET_KEY'] = "aQLgr7x3qbq1VDNqftqwX5YbGNh00oNDon2iIsvw"
app.secret_key = "M4eAXxf2Th3gXeMORdmla3v4G173LTgMMlZOaMth"

# DATABASE CONFIGRETION
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'

# csrf = CSRFProtect(app)
db = SQLAlchemy()
cache = Cache()
migrate = Migrate()

# INIT 
db.init_app(app)
migrate.init_app(app, db)

from .urls import *