# this is a function that takes in a file name and returns the idno as an object
# nowhere does it say that it takes in a string and returns a string; it just does

import elementtree.ElementTree as ET

def find_idno(xmlstring):

	root = ET.fromstring(xmlstring)

	#finds all five idnos!!! but searches whole publicationStmt
	idnos = root.findall('.//publicationStmt/idno') 
	# also valid: root.findall('.//idno')
	# inexplicably not valid: root.findall('.//teiHeader/biblFull/publicationStmt/idno')

	idnoVal = "you have a problem with find_idno"
	
	# let's use a loop now because ElementTree can't use XPATH
	for idno in idnos :
		if idno.attrib.get('type') == 'DLPS' :
			idnoVal = idno.text
			
	# returns the text of the idno element we're holding
	return idnoVal

	# IT WORKS! IT WORKS!