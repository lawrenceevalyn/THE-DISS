## set things up

# initate variables
sourcedirectory = "../corpora/ecco/ecco-tcp-plaintext-corpus"
targetdirectory = "../corpora/ecco-1789-99/ecco-tcp-1789-99-corpus"
sourcelist = "ecco-tcp-1789-99-names.txt"
problemcount = 0
copycount = 0


## run a program

# for each title in the list of titles
    # if a file with that filename exists,
         # copy it to the new directory
         copycount = copycount + 1
         print "found %s" % filename
     else
         problemcount = problemcount + 1
         print "couldn't find %s! oh no! problem!" % filename

print "finished copying files"
print "copycount: %d" % copycount
print "problemcount: %d" % problemcount