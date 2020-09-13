# this is a function that gets all the PUBLICATIONSTMT fields we care about

import collections
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

def publicationsTmt(xmlstring):
	
	root = ET.fromstring(xmlstring)
	PUBLICATIONSTMTs = root.findall('.//PUBLICATIONSTMT')

	TITLE = ""
	AUTHOR = ""
	PUBPLACE = ""
	PUBLISHER = ""
	
	for pub in PUBLICATIONSTMTs:
		TITLE_elements = pub.findall('.//TITLE')
		AUTHOR_elements = pub.findall('.//AUTHOR')
		PUBPLACE_elements = pub.findall('.//PUBPLACE')
		PUBLISHER_elements = pub.findall('.//PUBLISHER')
		if(TITLE_elements.length > 0)
			TITLE_element = TITLE_elements[0]
			TITLE = ET.tostring(TITLE_element, encoding="unicode")
		if(AUTHOR_elements.length > 0)
			AUTHOR_element = AUTHOR_elements[0]
			AUTHOR = ET.tostring(AUTHOR_element, encoding="unicode")
		if(PUBPLACE_elements.length > 0)
			PUBPLACE_element = PUBPLACE_elements[0]
			PUBPLACE = ET.tostring(PUBPLACE_element, encoding="unicode")
		if(PUBLISHER_elements.length > 0)
			PUBLISHER_element = PUBLISHER_elements[0]
			PUBLISHER = ET.tostring(PUBLISHER_element, encoding="unicode")

	# debugging
	print("TITLE = " + TITLE)
	print("AUTHOR = " + AUTHOR)
	print("PUBPLACE = " + PUBPLACE)
	print("PUBLISHER = " + PUBLISHER)

	Answer = collections.namedtuple('PUBLICATIONSTMTs', ['TITLE', 'AUTHOR', 'PUBPLACE', 'PUBLISHER']
	answer = Answer(TITLE, AUTHOR, PUBPLACE, PUBLISHER)
	return answer
