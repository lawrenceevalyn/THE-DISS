textsource = # must be a csv
randomsource = # must be a txt with one number per line
outputfile = textsource-randomsource.csv

for each line in randomsource
	sampleno = [the number on that line]
	get the line in textsource at sampleno
	append that line to outputfile
	
# is that all I need? this IS a really simple task...