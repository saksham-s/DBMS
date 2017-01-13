from sys import argv

#Opening meta-data file
with open('metadata.csv') as meta_file:
	meta_data = [line.rstrip('\n').split(',') for line in meta_file]
#Striping endline and spliting use comma
print meta_data
no_of_attr = len(meta_data)
print no_of_attr
with open('database.csv') as data_file:
	database = [line.rstrip('\n').split(',') for line in data_file]
	data_file.seek(0)
	print "Data in database:"
	print data_file.read()
if(len(argv)==2):
	print("Computing Sum:")
	print(argv[1])
else:
	print("Invalid argument!")