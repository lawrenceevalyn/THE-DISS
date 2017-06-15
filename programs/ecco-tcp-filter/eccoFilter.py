## set things up

# initate variables
sourcedirectory = "../corpora/ecco/ecco-tcp-plaintext-corpus"
targetdirectory = "../corpora/ecco-1789-99/ecco-tcp-1789-99-corpus"
sourcelist = "ecco-tcp-1789-99-names.txt"


## run a program

# for each title in the list of titles
    # if a file with that filename exists,
         print "found %s" $ filename
        # copy it to the new directory
     else
         pass