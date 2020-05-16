import os
import time
import shutil


present = time.time()

print("--------------------WELCOME--------------------\n"+
		"This Script will delete files that are older than 'x' number of days")


choice = input("Do You Want to Continue? (Y/N)\n"
				+"WARNING! THIS WILL DELETE ALL SPECIFIED FILES AND FOLDERS PERMANANTLY!!")


if(choice == 'y' or choice == 'Y'):

	days = int(input("Enter number of days old file to delete : "))

	seconds = days * 86400

	req = present - seconds

	flag = 0

	try:

		for files in os.listdir(os.getcwd()):
							
			if(os.path.getctime(files) < req):

				if(os.path.isfile(files)):
					os.remove(files)
				
				elif(os.path.isdir(files)):
					shutil.rmtree(files)

				print(files+" deleted!")
				
				flag = 1

		if(flag == 0):
			print("No Files Found!")

	except Exception as x:
		print("Unsuccessful! " + "Error Code : ")
		print(x)	