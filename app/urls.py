from app import app
from .views import *

@app.route("/")
def home():
	return Home()

@app.route("/profile/upload", methods=['GET','POST'])
def upload():
	return Upload()