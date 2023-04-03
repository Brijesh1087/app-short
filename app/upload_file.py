import random, os, mimetypes
from .auth import key, time


# GET FILE  TYPE
def file_type(filepath):
	file = mimetypes.guess_type(filepath)[0]
	if 'image' in file:
		return 'image'
	elif 'video' in file:
		return 'video'
	else:
		return False

# UPLOAD FIELS
def upload_file():
	return str(os.path.abspath(os.path.dirname((__file__))))

#  FILES  UPLOAD PATH
def file_path():
	return os.path.join(upload_file(),"static/store/media/")

# GET URL
def get_url(filepath, filename):
	path = f"{filepath}{key(10)}_{key(2)}_{filename}"
	return path

# FILE SIZE
def file_size(filepath):
	file_size = os.path.getsize(f"{os.path.abspath(os.path.dirname(__file__))}/{filepath}")
	size =  str(file_size/1024/1024)[:4]
	if float(size) <= 10 :
		if float(size) <= 9 and int(float(size)) >= 1 :
			re_size = "0"+size
			return re_size
		elif not "." in size:
			re_size = size+'.00'
			return re_size
		elif float(size) >= 10:
			return size
		else:
			re_size = "0"+size
			return re_size
	else:
		return False


