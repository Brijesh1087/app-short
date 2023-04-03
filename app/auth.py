import random, os, mimetypes
from datetime import datetime
# from upload_file import upload_file, file_type, file_size, files_path, get_url


char = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
def time():
	return str(datetime.now())[:19]

def key(length):
	temp = ""
	temp = random.choice(char[0:51])
	for x in range(1, length):
		temp += random.choice(char)
	return temp

