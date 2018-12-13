## set things up
#import libraries
import pandas as pd

# initate variables
# hard-code source since this doesn't need to be re-used
sourcefile = "../corpora/ECCO/combo-ECCO/all-nums-ECCO2A.csv"
targetfile = "../data/ecco-reprints/ecco-reprints.csv"

## run a program

data = pd.read_csv(sourcefile) #open the whole csv (bad idea?)

#discard the information that I won't care about for this process

#for each row in the csv,

	# Start by just doing it the dumb/easy way.
	# Look in columns 245 and 250 for the word "edition,"
		# If it's there,
			# grab the word to the left of that word
			# grab whatever's in 500 to add context
			# grab the book's title and author

	# add this info to the targetfile csv

# if I want to compare titles to each other, it will be way too inefficient
# to compare each titles to each other title; do it a less-stupid way