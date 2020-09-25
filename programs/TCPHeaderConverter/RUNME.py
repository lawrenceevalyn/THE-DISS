# As the name suggests, this is the main program that you need to run
# It will 'call' the other sub-programs as needed

# import libraries
import xml.etree.ElementTree as ET     # this makes it faster
import os.path
import collections
import csv
import operator

# import my other code
from find_idno import find_idno
from stripNamespace import stripNamespace
from fileDesc import fileDesc
from publicationsTmt import publicationsTmt

# things to store stuff in
fileDescList = []
publicationTmtList = []

#initiate variables
numfiles = 0
directory = "../../corpora/ECCO-TCP/ECCO-TCP-headers"

# make listdir ignore .DS_store (and other hidden files)
def listdir_nohidden(path):
    for f in os.listdir(path):
        if not f.startswith('.'):
            yield f

# iterate through the directory
for filename in listdir_nohidden(directory):

	# define the path to this file
	path = directory + "/" + filename

	# strip the file's namespace
	try:
		xmlstring = stripNamespace(path)
	except:
		print("error stripping namespace of file %s" % (filename))
	
	# call find-idno.py to print the file's TCP number
	# this is just so you can tell that the program's running,
	# and possibly see how far it got before it crashed (in case of problems)
#	try:
#		idno = find_idno(xmlstring)
#		print(idno)
#	except:
#		print("error finding IDNO with file %s" % (filename))

	# call fileDesc.py to get FILEDESC fields
	try:
		fileDescFields = fileDesc(xmlstring)
		fileDescList.append(fileDescFields)
	except:
		print("error getting fileDescFields for file %s" % (filename))
	
	# call publicationsTmt.py to get PUBLICATIONSTMT fields
#	try:
#		publicationsTmtFields = publicationsTmt(xmlstring)
#		publicationsTmtList.append(publicationsTmtFields)
#	except:
#		print("error getting publicationsTmtFields for file %s" % (filename))
		
	# increment a counter to see how many I read
	numfiles += 1

# print some stuff so you know what's going on
print("I read %d files" % (numfiles))

# time to start writing this stuff to the CSV!
newfilename = "tcpheaders-output.csv"
with open(newfilename,'w') as csvfile:
	fieldnames=['TITLE', 'AUTHOR', 'PUBPLACE', 'PUBLISHER', 'DLPS', 'ESTC','DocNo', 'TCP', 'GaleDocNo']
	writer=csv.writer(csvfile)
	writer.writerow(fieldnames)
	for i in range(numfiles):
		fd = fileDescList[i]
		pub = publicationsTmtList[i]
		writer.writerow(pub.TITLE, pub.AUTHOR, pub.PUBPLACE, pub.PUBLISHER, fd.DLPS, fd.ESTC, fd.DocNo, fd.TCP, fd.GaleDocNo)
	
