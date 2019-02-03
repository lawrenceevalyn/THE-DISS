import os

# HARD-CODE THESE BEFORE YOU DO ANYTHING
textsourcename = "testcorpus.csv" # must be a csv
randomsourcename = "testsample.txt" # must be a txt with one number per line


# This is the actual code that uses the info provided above

# open the source files
# textsource = open(textsourcename, "r")
# randomsource = open(randomsourcename, "r")

# automatically name output file based on inputs
outputfilename = ((os.path.splitext(textsourcename)[0])) + "-" + ((os.path.splitext(randomsourcename)[0])) + ".csv"

outputfile = open(outputfilename, "w") # creates blank output file
outputfile.close()					   # important so re-running rewrites!!

# make sure the files above work
#print ("textsource: ")
#print (textsourcename)
#print (textsource.read())

#print ("randomsource: ")
#print (randomsourcename)
#print (randomsource.read())

#print ("outputfile: ")
#print (outputfilename)
#print (outputfile.read())

# TIME TO LOOP
with open(randomsourcename) as fp: # can I do this in one line...?
	for line in fp: 
		
		# get the next number in the list
		sampleno = line
		print("sampleno: ")
		print(sampleno)
		
		# append that number to the output file
		# (later change this so it appends the desired data from textsource)
		fh = open(outputfilename, "a")
		fh.write(sampleno) # this is the thing to change what gets appended
		fh.close()

print ("outputfile: " + outputfilename)
fo = open(outputfilename, "r")
print (fo.read())
fo.close()

#	get the line in textsource at sampleno
#	append that line to outputfile