import sys
reload(sys)  # Reload is a hack

import mysql.connector
from mysql.connector import errorcode

sys.setdefaultencoding('UTF8')
from asd import detect_text
from asd import emailExtractor
import ImagesClass as imObj
import filePathFinder as files
import time, sys
import glob,os

#For file processing on the terminal screen
def update_progress(job_title, progress):
    length = 20 # modify this to change the length
    block = int(round(length*progress))
    msg = "\r{0}: [{1}] {2}%".format(job_title, "#"*block + "-"*(length-block), round(progress*100, 2))
    if progress >= 1: msg += " DONE\r\n"
    sys.stdout.write(msg)
    sys.stdout.flush()


# class ImageExtractor():
def main(image_obj_list):
	image_list = []
	files.filePathFinder(image_list)

	try:
		cnn = mysql.connector.connect(user='seniorProject', password='seniorProject', host='127.0.0.1',
									  database='csiresume')
		print("It works!")
	except mysql.connector.Error as e:
		if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
			print("Sth is wrong with username or pw")
		elif e.errno == errorcode.ER_BAD_DB_ERROR:
			print("DB does not exist")
		else:
			print(e)

	cursor = cnn.cursor()

	print(image_list)
	ebe = 0

	for i in range(0,len(image_list)):
		# print(image_list[i])
		# print("Read number: "+str(i))
		text = detect_text(image_list[i]) #0 deggil databasede olmayan imagein indexi
		key = emailExtractor(text)

		str(text).encode('utf-8')
		update_progress("Resumes are being processed",i/float(len(image_list)))

		if(str(key).find("unid@unid.com")!=-1):
			ebe+=1
		else:
			image_obj_list.append(imObj.Images(key,text))

			fin = open(str(image_list[i]))
			image = fin.read()

			try:
				query = ("INSERT INTO ResumeImages VALUES (%s, %s)")
				cursor.execute(query,(str(key).replace("[", "").replace("'", "").replace("]", ""),image))
				cnn.commit()

			except mysql.connector.IntegrityError:
				query = "UPDATE ResumeImages SET ResImage = %s WHERE ID= %s"
				cursor.execute(query, (image,str(key).replace("[", "").replace("'", "").replace("]", "")))
				cnn.commit()
				continue

	cursor.close()
	cnn.close()

	for i in range(0,len(image_list)):
		os.remove(image_list[i])

	update_progress("Resumes are being processed",1)

