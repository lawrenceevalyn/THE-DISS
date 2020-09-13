# this makes the file into a string without its namespace (so it can be used elsewhere)

import re

def stripNamespace(path):
	# open the file and convert it to a string
	with open(path, 'r') as myfile:
		xmlstring=myfile.read()
    
		# use a regex! say a prayer
		xmlstring = re.sub(' xmlns="[^"]+"', '', xmlstring)
		
		# add the xml version and unicode encoding
		# I think actually our unicode problems came at the writing stage, not here
		# but why not?
		xmlstring = '<?xml version="1.0" encoding="utf-8"?>' + xmlstring
		
	return xmlstring