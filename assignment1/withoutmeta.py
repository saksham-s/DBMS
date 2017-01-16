from sys import argv,exit


import time
start_time = time.time()





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
	no_of_attr=len(database[0])
	for i in range(no_of_attr):
		if(database[0][i]==argv[1]):
			field_name = database[0][i]
			index=i
			present=1
			break
	if(present==0):
		print "Attribute not present"
		exit()

	print "Attribute Found."
	print field_name
	#add more
	if(field_name=='ID'):
		for j in range (1,len(database)):
				sum+=int(database[j][i])
		print "SUM is: ",sum
	elif(field_name=='Price'):
		for j in range (1,len(database)):
				sum+=float(database[j][i])
		print "SUM is: ",sum
	else:
		print "Character type argument!"

else:
	print "Invalid argument!"


print("Execution time is --- : %s seconds ---" % (time.time() - start_time))