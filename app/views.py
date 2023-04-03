from flask import render_template, request, redirect, url_for
from app import db, cache
from .models import UploadVideo
from .upload_file import key, file_size, file_type, get_url, upload_file, file_path, time

def Home():
	return render_template('index.html')

def Upload():
	return render_template('profile/upload.html')