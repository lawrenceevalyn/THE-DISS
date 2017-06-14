## This file contains all that you need to setup and run your first topic model. 
## It will build a 50 topic model from the specified source folder. 
## See https://www.cs.princeton.edu/~blei/lda-c/index.html

## Adapted from Neal Audenart's "First Topic Models" example_1.R program

source("functions/lda.R")
source("functions/import.R")

# The directory from which to import data (change name to change data source)
data.dir <- "corpora/titles/estc-1789-99-titles"

# This loads the documents from the directory above in a format that can be used 
# with Mallet.
docs <- loadDocuments(data.dir);

# Specify a set of stop-words, or commonly used words to be removed from the documents
# in order to improve model performance.
stoplist <- "dhsi-2017/TopicModelingRTools/stop-words/stop-words_english_3_en.txt"

# Train a document model with 50 topics. This will run Mallet over the documents
# from data.dir and store the results along with some supporting information 
# in a convenient data structure
model <- trainSimpleLDAModel(docs, 50, stoplist=stoplist)

# Print the resulting topics as wordclouds for easy visualization.
print("printing topic word clouds")
plotTopicWordcloud(model, verbose=T)
