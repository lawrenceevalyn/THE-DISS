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

def fileDesc(xmlstring):
	
	root = ET.fromstring(xmlstring)

	DLPS = ""
	ESTC = ""
	DocNo = ""
	TCP = ""
	GaleDocNo = ""

	IDNOs = root.findall('.//FILEDESC/PUBLICATIONSTMT/IDNO')
	print("found IDNOs")
	for IDNO in IDNOs:
		print("got IDNO")
		print(IDNO.tag, IDNO.attrib)
		print(IDNO.text)
		if IDNO.attrib == "DLPS":
			DLPS = IDNO.text
			print("DLPS is " + DLPS)
		elif IDNO.attrib == "ESTC":
			ESTC = IDNO.text
			print("ESTC is " + ESTC)
		else:
			print("it's not DLPS or ESTC")	
				
#older, clumsier version (which didn't even work)
#	FILEDESCs = root.findall('.//FILEDESC')
#	for FILEDESC in FILEDESCs:
#		PUBLICATIONSTMTs = FILEDESC.findall('.//PUBLICATIONSTMT')
#		#print("inside filedesc")
#		for PUBLICATIONSTMT in PUBLICATIONSTMTs:
#			print("inside publicationstmt")
#			#the IDNO tags have an attribute with the value "type",
#			# and for each IDNO "type" I want to get the tag content
#			ESTC = PUBLICATIONSTMT.findtext(".//IDNO[@type='ESTC']")
#			print(ESTC)



	Answer = collections.namedtuple('IDNOs', ['DLPS', 'ESTC', 'DocNo', 'TCP', 'GaleDocNo'])
	answer = Answer(DLPS, ESTC, DocNo, TCP, GaleDocNo)
	return answer
