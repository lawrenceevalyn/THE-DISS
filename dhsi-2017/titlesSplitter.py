# This Python file uses the following encoding: utf-8

# initialize variables
filepath = "ecco-tcp-1789-99-titles.txt" # change as needed
loopcounter = 0

# go through the list of titles and split it on newlines
with  open(filepath) as fp:
    contents = fp.read()
    for entry in contents.split('\n'):
        print entry # just to be sure it's working
        loopcounter = loopcounter + 1 
        print "loopcounter: %d" % loopcounter # make sure it does all of them
        
        # make new files out of each title
        filename = ("ecco-title%d.txt" % loopcounter)     # change name here too
        file = open(filename,"w") # files will spit out annoyingly
        file.write(entry)         # in same directory as the program;
        file.close()              # move the program around accordingly
                                  # (since there will be a lot of files to move)