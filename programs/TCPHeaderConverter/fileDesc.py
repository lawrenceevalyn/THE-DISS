# this is a function that gets all the FILEDESC IDNO fields we care about
	#from within FILEDESC > PUBLICATIONSTMT tags:
		#IDNO type=DLPS
		#IDNO type=ESTC
		#IDNO type=DocNo
		#IDNO type=TCP
		#IDNO type=GaleDocNo

import collections
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

#using the tuple because it's basically a dictionary but we know the keys
#this defines the type
FileDescReturnType = collections.namedtuple('IDNOs', ['DLPS', 'ESTC', 'DocNo', 'TCP', 'GaleDocNo'])

#defining a function that will return FileDescReturnType
def fileDesc(xmlstring) -> FileDescReturnType:
	
	root = ET.fromstring(xmlstring)

	DLPS = ""
	ESTC = ""
	DocNo = ""
	TCP = ""
	GaleDocNo = ""

	IDNOs = root.findall('.//FILEDESC/PUBLICATIONSTMT/IDNO')
	#print("found IDNOs")
	for IDNO in IDNOs:
		#print("got IDNO")
		#print(IDNO.tag, IDNO.attrib)
		#print(IDNO.text)
		if IDNO.attrib["TYPE"] == "DLPS":
			DLPS = IDNO.text
			#print("DLPS is " + DLPS)
		elif IDNO.attrib["TYPE"] == "ESTC":
			ESTC = IDNO.text
			#print("ESTC is " + ESTC)
		elif IDNO.attrib["TYPE"] == "DocNo":
			DocNo = IDNO.text
			#print("DocNo is " + DocNo)
		elif IDNO.attrib["TYPE"] == "TCP":
			TCP = IDNO.text
			#print("TCP is " + TCP)
		elif IDNO.attrib["TYPE"] == "GaleDocNo":
			GaleDocNo = IDNO.text
			#print("GaleDocNo is " + GaleDocNo)
		#else:
			#print("it's not one of the IDNOs I know")	
	
	#shoves our data into an object so we can return it
	answer = FileDescReturnType(DLPS, ESTC, DocNo, TCP, GaleDocNo)
	return answer
