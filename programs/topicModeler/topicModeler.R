## This file contains all that you need to setup and run your first topic model. 
## It will build a topic model from the specified source folder. 
## See https://www.cs.princeton.edu/~blei/lda-c/index.html

## Adapted from Neal Audenart's "First Topic Models" example_1.R program

# Always start by running this command:
# dyn.load('/Library/Java/JavaVirtualMachines/jdk1.8.0_131.jdk/Contents/Home/jre/lib/server/libjvm.dylib')
# Make sure the java version is correct in the url above!

# To run a few lines: select them and click "Run"
# To run the whole program: click "Source" (even though this makes no sense)

# Run these first just to be sure erverything is working
source("functions/lda.R")
source("functions/import.R")
# If it can't find files, make sure directory structure makes sense
# from the POV of the .Rproj file

# Specify a set of stop-words, or commonly used words to be removed from the
# documents in order to improve model performance.
stoplist <- "stop-words/18thC_titles_stopwords.txt"

# The directory from which to import data (change name to change data source)
data.dir <- "../../../corpora/titles/ecco-tcp-1789-99-titles"

# This loads the documents from the directory above in a format that can be used 
# with Mallet.
docs <- loadDocuments(data.dir);

# Train a document model with specified # of topics. This will run Mallet over the
# documents from data.dir and store the results along with some supporting information 
# in a convenient data structure
model <- trainSimpleLDAModel(docs, 30, stoplist=stoplist)

# Print the resulting topics as wordclouds for easy visualization.
print("printing topic word clouds")
plotTopicWordcloud(model, verbose=T)
