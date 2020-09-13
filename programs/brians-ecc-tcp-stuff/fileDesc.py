# this is a function that gets all the FILEDESC IDNO fields we care about

import collections
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

def fileDesc(xmlstring):
	
	root = ET.fromstring(xmlstring)

	DLPS = ""
	ESTC = ""
	DocNo = ""
	TCP = ""
	GaleDocNo = ""

	FILEDESCs = root.findall('.//FILEDESC')
	for FILEDESC in FILEDESCs:
		IDNOs = FILEDESC.findall('.//IDNO')
		print("hi")
		for IDNO in IDNOS:
			print("something")
			DLPS_elements = IDNO.findall('.//DLPS')
			ESTC_elements = IDNO.findall('.//ESTC')
			DocNo_elements = IDNO.findall('.//DocNo')
			TCP_elements = IDNO.findall('.//TCP')
			GaleDocNo_elements = IDNO.findall('.//GaleDocNo')
			if(DLPS_elements.length > 0):
				DLPS_element = DLPS_elements[0]
				DLPS = ET.tostring(DLPS_element, encoding="unicode")
			if(ESTC_elements.length > 0):
				ESTC_element = ESTC_elements[0]
				ESTC = ET.tostring(ESTC_element, encoding="unicode")
			if(DocNo_elements.length > 0):
				DocNo_element = DocNo_elements[0]
				DocNo = ET.tostring(DocNo_element, encoding="unicode")
			if(TCP_elements.length > 0):
				TCP_element = TCP_elements[0]
				TCP = ET.tostring(TCP_element, encoding="unicode")
			if(GaleDocNo_elements.length > 0):
				GaleDocNo_element = GaleDocNo_elements[0]
				GaleDocNo = ET.tostring(GaleDocNo_element, encoding="unicode")

	# debugging
	print("DLPS = " + DLPS)
	print("ESTC = " + ESTC)
	print("DocNo = " + DocNo)
	print("TCP = " + TCP)
	print("GaleDocNo = " + GaleDocNo)

	Answer = collections.namedtuple('IDNOs', ['DLPS', 'ESTC', 'DocNo', 'TCP', 'GaleDocNo'])
	answer = Answer(DLPS, ESTC, DocNo, TCP, GaleDocNo)
	return answer
