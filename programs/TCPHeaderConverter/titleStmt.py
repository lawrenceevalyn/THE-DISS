# this is a function that gets all the TITLESTMT fields we care about
#	from within FILEDESC > SOURCEDESC > BIBLFULL > TITLESTMT tags:
#		TITLE
#		AUTHOR

import collections
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

#using the tuple because it's basically a dictionary but we know the keys
#this defines the type
titleStmtReturnType = collections.namedtuple('TITLESTMTs', ['TITLE', 'AUTHOR'])

def titleStmt(xmlstring) -> titleStmtReturnType:
	#print("debug 0")	
	root = ET.fromstring(xmlstring)
	TITLESTMTs = root.findall('.//FILEDESC/SOURCEDESC/BIBLFULL/TITLESTMT')

	TITLE = ""
	AUTHOR= ""
	
	#print("debug 1")
	for title in TITLESTMTs:
		#print("debug 1.5")
		TITLE_elements = title.findall('.//TITLE')
		AUTHOR_elements = title.findall('.//AUTHOR')
		#print("debug 2")
		if(len(TITLE_elements) > 0):
			TITLE_element = TITLE_elements[0]
			TITLE = TITLE_element.text
			#print("debug 3")
		if(len(AUTHOR_elements) > 0):
			AUTHOR_element = AUTHOR_elements[0]
			AUTHOR = AUTHOR_element.text
			#print("debug 4")

	# debugging
	#print("TITLE = " + TITLE)
	#print("AUTHOR = " + AUTHOR)

	answer = titleStmtReturnType(TITLE, AUTHOR)
	return answer
