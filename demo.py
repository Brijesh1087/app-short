# import os, mimetypes

# # os.remove(("hellopath")
# # # filename = "example.mp4"
# filename = "8.jpeg"
# file_type = mimetypes.guess_type(filename)[0]

# # # get file size
# # file_size = os.path.getsize(filename)
# # print("File size: ", file_size, "bytes")
# # print(file_type)
# # # get file type
# # file_type = os.path.splitext(filename)
# # print("File type: ", file_type)
# # for x in dir(os.path):
# 	# print(x)
# # print(os.getcwd())

# # print("hello".join('.'))


# # import os

# # get the absolute path of the base directory
# base_path = os.path.abspath(os.path.dirname(__file__))

# # get the current working directory
# current_path = os.getcwd()

# # join the base and current paths together
# full_path = os.path.join(base_path, 'static_folder')

# # print("Full path:", full_path)
# # print("Base path:", base_path)
# # print("Current path:", current_path)
# print(os.path.dirname(__file__))
# print(os.path.abspath(os.path.dirname(__file__)))





if request.method == 'POST':
		file = request.files['file']
		desc = request.form['desc']
		cate = request.form['cate']
		user = 'jeamy-sames'
		video_path  = os.getcwd()
		image_path  = os.getcwd()

		if os.path.exists(f"/app{video_path}/{user}"):
			video_path = f"/app{video_path}/{user}/"
		else:
			os.mkdir(f"{video_path}/{user}")
			video_path = f"/app{video_path}/{user}/"

		if os.path.exists(f"/app{image_path}/{user}"):
			image_path = f"/app{image_path}/{user}/"
		else:
			os.mkdir(f"{image_path}/{user}")
			image_path = f"{image_path}/{user}/"

		remove_file = ""
		file_path = "" 

		if file_type(file.filename):
			video_duration = ""
			if file_type(file.filename) == 'image':	
				url_re_name =get_url(image_path, file.filename) 
				file.save(url_re_name)
				remove_file = url_re_name
				file_path = url_re_name
			else:
				url_re_name =get_url(video_path, file.filename) 
				file.save(url_re_name)
				remove_file = url_re_name
				file_path = url_re_name
				video_duration = get_file_size(image_path)
			# print(remove_file,"FILESIZE")
			if get_file_size(file_path):
				add_video = UploadVideo(user=user, video_src=f'{remove_file}', time_line=time(), key=key(20), cate=cate, desc=desc, url=file_path, thumnail=f'{remove_file}', video_duration=video_duration)
				db.session.add(add_video)
				db.session.commit()
				db.session.close()
				return render_template("profile/upload.html")
			else:
				os.remove(f'{remove_file}')
				# os.remove(f'{video_path}/{file.filename}')
				return render_template("profile/upload.html")
		else:
			return render_template("profile/upload.html")


	else:
		return render_template("profile/upload.html")
