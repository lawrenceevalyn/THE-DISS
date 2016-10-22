#TODO: better handling of files (i.e., probably don't store it in a string...?)
#TODO: make it run through a whole directory of files (see: XML-parser for Holger)
#TODO: Consider removing:
    # punctuation marks?
    # single letters?
    # "chapter" and "vol"/"volume"?
    # the word "page" (due to Zofloya)?

#TODO: would it help to remove everything that's not in a dictionary?
# except for words that are capitalized? (to preserve names)
# it would be just like reading a moldy manuscript that's missing key details and cuts off right at a cliffhanger...

# -*- coding: utf-8 -*-
		# declare that this file uses Unicode literals (?)

import re
		# import regular expressions

book = open('bad01.txt').read()
		# read bad01.txt and hold it in the string book

book = re.sub('- ', '', book)
		# delete hyphen-space combos

book = re.sub('¬ ','', book)
		# delete ¬-space combos

book = re.sub('-\n','', book)
		# delete hyphen-newline combos
		
book = re.sub('\n',' ', book)
		# replace newlines with space
		
book = re.sub('[^a-zA-Z\.]', ' ', book)
		# substitute a space for everything that isn't a letter or period
		# (this means it deletes newlines)

book = re.sub('vv', 'w', book)
		# change 'vv' to 'w'
		
book = re.sub('s', 'f', book)
		# change all Ss to Fs to reduce ambiguity
		
book = re.sub('Disclaimer: This file is generated from OCR (optical character recognition), which is a technology that converts images of text into text. While the technology is good at deciphering legible text, there are limitations and some text may not have been extracted correctly.','', book)
		# delete Corvey disclaimer text
		
open('fixed01.txt', 'w').write(book) 
		# write fixed01.txt with book