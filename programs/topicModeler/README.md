# Set-up

Start by opening TopicModelingRTools.Rproj

iif there are java problems, run this, making sure to have the right version number in the URL:
dyn.load('/Library/Java/JavaVirtualMachines/jdk1.8.0_**131**.jdk/Contents/Home/jre/lib/server/libjvm.dylib')

run these two lines to check that it's working (select and click "Run"):
```source("functions/lda.R")
source("functions/import.R")
```

Click "source" to run the program itself. Remember the filepaths etcs are all determined from the POV of the the Rproj file, not the individual R program!

# R commands cheatsheet

```topic.23 <- model$getTopic(23)```
get set up to look deeply at a particular topic (#23)

```topic.23$getWords(10)```
gets the top 10 words predictive of that topic

```topic.23$getDocs(10)```
gets the documents with the highest proportions of that topic

```top.docs <- topic.23$getDocs(10)```
make a list of top 10 documents for a topic

`model$getDocument(names(top.docs[4]))` gets 4th article in top 10 article list, displays the document itself

## To get data out of R:

Can use `View(model$topics)` or `View(model$docAssignments)` (note capital V) to see matrix of numbers in Rstudio

`write.table(model$topics, file="FILENAME.csv", sep=",", row.names=T)` - to save words-in-topics

`write.table(model$docAssignments, file="FILENAME.csv", sep=",", row.names=T)` - to save topics-in-documents

`plotTopicWordcloud(model)` - to make wordclouds

## Working with CSV

Find CSV in data directory, click in R's file management and say "import dataset"

```
library(readr)
estc_1789_1799_enk <- read_csv("~/Desktop/THE-DISS/corpora/estc/estc_1789-1799_enk.csv")
View(estc_1789_1799_enk)
```

Need to have an "id" column and a "text" column

Can see what the columns are currently named: ```colnames(estc_1789_1799_enk)```

Can rename column just in Rstudio instead of in csv: ```colnames(estc_1789_1799_enk)[2] <- id```

## How I Got A Visualization To Work

First, create a topic model called "model" (via any method you prefer)

`install.packages("LDAvis")`

`library(LDAvis)`

`help(createJSON, package = "LDAvis")` - to see what everything needs

`doc.lengths <- sapply(model$documents$text, nchar)` -  the only variable you need to create in advance

`json <- createJSON(phi = model$topics, theta = model$docAssignments, doc.length = doc.lengths, vocab = model$vocabulary, term.frequency = model$wordFreq$term.freq, R = 30, lambda.step = 0.01, mds.method = jsPCA, plot.opts = list(xlab ="PC1", ylab = "PC2"))` - this actually creates the JSON file, and will take a while to run

`serVis(json)` - this launches the visualization in a browser!