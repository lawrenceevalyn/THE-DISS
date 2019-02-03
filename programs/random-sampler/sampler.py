import os

# HARD-CODE THESE BEFORE YOU DO ANYTHING
textsourcename = "testcorpus.csv" # must be a csv
randomsourcename = "testsample.txt" # must be a txt with one number per line


# This is the actual code that uses the info provided above

# automatically name output file based on inputs
outputfilename = ((os.path.splitext(textsourcename)[0])) + "-" + ((os.path.splitext(randomsourcename)[0])) + ".csv"

outputfile = open(outputfilename, "w") # creates blank output file
outputfile.close()					   # important so re-running rewrites!!

# TIME TO LOOP
with open(randomsourcename) as fp: # can I do this in one line...?
	for line in fp: 
		
		# get the next number in the list
		sampleno = line
		print("sampleno: ")
		print(sampleno)
		
		# get the line in textsource at sampleno
		
		# append sampleno to the output file
		# (later change this so it appends the desired data from textsource)
		fh = open(outputfilename, "a")
		fh.write(sampleno) # this is the thing to change what gets appended
		fh.close()

print ("outputfile: " + outputfilename)
fo = open(outputfilename, "r") # file handling is so weird and I hate it
print (fo.read())			   # but this lets me check that the right thing
fo.close()					   # ended up in the output file