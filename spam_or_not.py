import os
import re
import random
import string

#finding current path
current_dir = cwd = os.getcwd()

"""This if condition is unnecessary but if I run code to another directory it raises error.
so used this to ensure whether the directory is availabe or not."""
if os.path.isdir(current_dir+"/files/"):
	pass
else:
	#creating path
	os.mkdir(current_dir+"/files/")

#listing all the files in the directory
arr = os.listdir(current_dir+"/files/")

#looping listed files
for i in arr:
	def randomString(stringLength):

	    """Generate a random string of fixed length """
	    letters = string.ascii_lowercase
	    return ''.join(random.choice(letters) for j in range(stringLength))+".txt"

	def saveFile(path):

		file_name = randomString(4)
		file = path + file_name
		#check whether the same file name exist or not
		if os.path.exists(file):
			file_name = randomString(4)
        #creating new file
		create_file = open(file, "x")
		#copying content from old file to new one
		with open(current_dir+"/files/"+i) as old_file:
			with open(file, "w") as new_file:
				for line in old_file:
					new_file.write(line)

	def path(path):
        #check whether the directory is exist or not. If not exist creating new one
		if os.path.isdir(path):
			saveFile(path)
		else:
			os.mkdir(path)
			saveFile(path)

	spam_path = current_dir+"/spam/"
	other_file_path = current_dir+"/normal/"

	f = open(current_dir+"/files/"+i, "r")
	"""By using regular expresiion finding spam words"""
	r = [re.findall(r'\bsex\b | \bLOTTERY\b | \bCASHBACK\b',line,flags=re.I) for line in open(current_dir+"/files/"+i)]

   #checkig current file is spam or not
	if(len(r[0]) != 0):
		path(spam_path)	
	else:
		path(other_file_path)


	