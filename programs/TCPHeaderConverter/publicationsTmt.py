# this is a function that gets all the PUBLICATIONSTMT fields we care about
#	from within FILEDESC > SOURCEDESC > BIBLFULL > PUBLICATIONSTMT:
#		DATE
#		PUBPLACE
#		PUBLISHER

import collections
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

#using the tuple because it's basically a dictionary but we know the keys
#this defines the type
publicationsTmtReturnType = collections.namedtuple('PUBLICATIONSTMTs', ['DATE', 'PUBPLACE', 'PUBLISHER'])

def publicationsTmt(xmlstring) -> publicationsTmtReturnType:
	#print("debug 0")	
	root = ET.fromstring(xmlstring)
	PUBLICATIONSTMTs = root.findall('.//FILEDESC/SOURCEDESC/BIBLFULL/PUBLICATIONSTMT')

	DATE = ""
	PUBPLACE = ""
	PUBLISHER = ""
	
	#print("debug 1")
	for pub in PUBLICATIONSTMTs:
		#print("debug 1.5")
		DATE_elements = pub.findall('.//DATE')
		PUBPLACE_elements = pub.findall('.//PUBPLACE')
		PUBLISHER_elements = pub.findall('.//PUBLISHER')
		#print("debug 2")
		if(len(DATE_elements) > 0):
			DATE_element = DATE_elements[0]
			DATE = DATE_element.text
			#print("debug 3")
		if(len(PUBPLACE_elements) > 0):
			PUBPLACE_element = PUBPLACE_elements[0]
			PUBPLACE = PUBPLACE_element.text
			#print("debug 4")
		if(len(PUBLISHER_elements) > 0):
			PUBLISHER_element = PUBLISHER_elements[0]
			PUBLISHER = PUBLISHER_element.text
			#print("debug 5")

	# debugging
	#print("DATE = " + DATE)
	#print("PUBPLACE = " + PUBPLACE)
	#print("PUBLISHER = " + PUBLISHER)

	answer = publicationsTmtReturnType(DATE, PUBPLACE, PUBLISHER)
	return answer
