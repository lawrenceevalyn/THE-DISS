take in a directory and filename

discard the information that I won't care about for this process

for each row in the csv,

	it would be way too inefficient to compare it to every other row in the csv,
	since there are 50k, so do something less stupid.

	Start by just doing it the dumb/easy way.
	Look in columns 245 and 250 for the word "edition,"
		If it's there,
			grab the word to the left of that word
			grab whatever's in 500 to add context
			grab the book's title and author