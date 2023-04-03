from app import db

model = db.Model
column = db.Column
integer = db.Integer
string = db.String
json = db.JSON
boolean = db.Boolean


# upload vides
class UploadVideo(model):
	__tablename__ =  'uploadvideo'

	def __init__(self, user ,file_src, time_line, key, cate, desc, url, video_duration):
		self.user = user
		self.file_src = file_src
		self.time_line = time_line
		self.key = key
		self.cate = cate
		self.desc = desc
		self.url = url
		self.video_duration = video_duration

	id = column(integer(), primary_key=True)
	user = column(string, nullable=False)
	file_src =column(string, nullable=False, unique=True)
	time_line = column(string, nullable=False)
	key = column(string, nullable=False, unique=True)
	cate = column(string, nullable=False)
	desc = column(string, nullable=False)
	url = column(string, nullable=False ,unique=True)
	video_duration = column(string)

