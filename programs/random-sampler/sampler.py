# HARD-CODE THESE BEFORE YOU DO ANYTHING
textsourcename = "testcorpus.csv" # must be a csv
randomsourcename = "testsample.txt" # must be a txt with one number per line

# This is the actual code that uses the info provided above
#outputfilename = textsource + "-" + randomsource
#outputfile = outputfilename.csv

textsource = open(textsourcename, "r")
randomsource = open(randomsourcename, "r")

print ("textsource: ")
print (textsourcename)
print (textsource)

print ("randomsource: ")
print (randomsourcename)
print (randomsource)

# print "outputfile: " + outputfile

#for each line in randomsource
#	sampleno = [the number on that line]
#	get the line in textsource at sampleno
#	append that line to outputfile
	
# is that all I need? this IS a really simple task...