# Reminder to self: the way R works is that you essentually run the code yourself,
# line by line, rather than following the python workflow of running whole "programs".
# Think of this as a place to keep scratch notes, rather than a program,
# and copy output from the console to long-term storage.

### Set up every time ###

library(gender) # re-run this every time to remind R that it knows this plugin
# install_genderdata_package() # don't need these every time, but if it doesn't work
# devtools::install_github("ropensci/genderdata") # these can reinstall it

# then, set the working directory to where the data is (Session>Set Working Directory)
setwd("~/Desktop/desktop/THE-DISS/corpora/ECCO/Digital-Scholar-Lab")

### Actual Code Stuff ###

ECCO1789 <- read.csv("ECCO-1789_metadata-firstnames.csv")
# this works on the sample but not on the full data
# easier to change data so it has a "firstname" column rather than telling R to just look at some stuff
View(ECCO1789) # just to look at it
ECCO1789names <- as.character(ECCO1789$First.name)
ECCO1789names # just to look at it


gender(ECCO1789names, method = "ipums", years = 1799)
# if this makes an empty tibble, it's probably fine, but I'm asking for something it has no data for (probably because the date is too early)
# ipums can go as early as 1789
# napp can go as early as 1758, but doesn't know the name "John" until 1769

ECCO1789results <- gender(ECCO1789names, method = "ipums", years = 1799) # to put those results in a table
write.csv(ECCO1789results)

## for troubleshooting ##
testnames = c("john", "madison")  #just to check it works at all if needed