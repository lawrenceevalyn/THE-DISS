## Why NOT build a topic modeler from the ground up to do the thing I want to do?
## Adapted from Neal Audenart's "First Topic Models" example_1.R program

# Always start by running this command:
# dyn.load('/Library/Java/JavaVirtualMachines/jdk1.8.0_131.jdk/Contents/Home/jre/lib/server/libjvm.dylib')
# Make sure the java version is correct in the url above!

# import functions
source("functions/lda.R")
source("functions/import.R")
# Run these first just to be sure everything is working
# If it can't find files, make sure directory structure makes sense
# from the POV of the .Rproj file (NOT the POV of R program)

# specify stop-words
stoplist <- "stop-words/18thC_titles_stopwords.txt"

# specify source directories
estc-data.dir <- "../../../corpora/titles/estc-1789-99-titles"
estc-docs <- loadDocuments(data.dir);
ecco-data.dir <- "../../../corpora/titles/ecco-tcp-1789-99-titles"
ecco-docs <- loadDocuments(data.dir);

# do some topic modeling!

# 1. train a document model on ESTC with specified # of topics
model <- trainSimpleLDAModel(estc-docs, 50, stoplist=stoplist)

# 2. output ESTC topics, doc topic counts, and wordclouds
# print the resulting topics as wordclouds for easy visualization
print("printing topic word clouds")
plotTopicWordcloud(model, verbose=T)

# 3. run topics over ECCO

# 4. output ECCO topics, doc topic counts, and wordclouds
