# set things up

# make listdir ignore .DS_store (and other hidden files)
def listdir_nohidden(path):
    for f in os.listdir(path):
        if not f.startswith('.'):
            yield f

# initate variables
directory = "DIRECTORYNAME"



# for each file in the full ecco directory,
for filename in listdir_nohidden("./" + directory):

    # define the path to this file
    path = "./" + directory + "/" + filename

# compare its filename to the list of names in ecco-tcp-1789-99.txt
    # if the name appears anywhere on the list,
        # copy the file to the ecco-1789-99 directory
    # else
        # pass