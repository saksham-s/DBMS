from sys import argv,exit

import time
start_time = time.time()
#Opening meta-data file
with open('metadata.csv') as meta_file:
	meta_data = [line.rstrip('\n').split(',') for line in meta_file]
#Striping endline and spliting use comma
print meta_data
no_of_attr = len(meta_data)
print "Number of attributes: ",no_of_attr
with open('database.csv') as data_file:
	database = [line.rstrip('\n').split(',') for line in data_file]
	data_file.seek(0)
	print "Data in database:"
	print data_file.read()
sum=0
if(len(argv)==2):
	print("Computing Sum:")
	print(argv[1])
	present = 0
	for i in range(no_of_attr):
		if(meta_data[i][0]==argv[1]):
			field_name = meta_data[i][0]
			field_data_type = meta_data[i][1]
			field_size = meta_data[i][2]
			present=1
			break
	if(present==0):
		print "Attribute not present"
		exit()

	print "Attribute Found."
	print field_name,field_data_type,field_size
	#add more
	if(field_data_type=='I'):
		for j in range(0,len(database[0])):
			if(database[0][j]==field_name):
				column=j
				break
		for j in range (1,len(database)):
				sum+=int(database[j][column])
		print "SUM is: ",sum
	elif(field_data_type=='F' or field_data_type=='D'):
		for j in range(0,len(database[0])):
			if(database[0][j]==field_name):
				column=j
				break
		for j in range (1,len(database)):
				sum+=float(database[j][column])
		print "SUM is: ",sum
	else:
		print "Sum cannot be computed for this argument,because either it is not present or is non numeric!"

else:
	print "Invalid argument!"



print("Execution time is --- : %s seconds ---" % (time.time() - start_time))
