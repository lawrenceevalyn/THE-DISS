# Understanding Topic Modeling
### with Neal Audenaert
<!-- neal.audenaerte@gmail.edu -->

## June 12 2017

Relieved to hear that Neal also comes to topic modelling from a fairly skeptical perspective -- but lately people are using it in pretty sophisticated, less black-box-y ways

Sometimes the thing that's easier IS to pull the spreadsheet open in excel, instead of taking six weeks to write a program

Another mention of DocuScope - I should try it

(Seems the buckets-with-training-texts approach is really unusual here)

Topic modeling removes one source of human bias -- ensures even attention to various kinds of features, etc -- but introduces new sources in set-up and analysis

Biggest challenge is analysis of results

The key to collaborating is to know enough, but not to try to know everything -- the best work requires more expertise than one person can have

### Topic Modelling! What it is!

Given a set of documents; we assume that there is some internal organization (topics) that we want to model computationally

What is a model? A representation and simplification, for a purpose

The set of documents is organized, understood to some level, and we have questions about them; we want to build a model that is meaningful (we can actually interpret it), useful, and approximate (not pure objective truth; can't answer really precise, fine-grained questions)

(Problem with sentiment analysis -- not usually actually meaningful! **Brand identity managers** care a lot, but for humanities research it's rarely what we want. Pleased to see confirmation that this isn't a useful direction to steer our collaboration unless we're using sentiment as a classifying tool for something else, rather than directly asking about sentiment)

Main source: Latent dirichlet allocation, DM Blei - 2003
Big idea: Documents exhibit multiple topics!

If I'm talking about topic X, I'm likes to use words Y and Z at various probabilities

Got a bunch of topics in the world, and pretend we know what they are in advance. There are fifty topics in the world!

Then we have a document, which exhibits multiple topics in different proportions

The words in the document are each tied to a specific topic... the model can't handle the idea that a word might reference multiple topics

In practice one of the topics is often going to be junk; conveniently the weird random stuff mostly clustered together -- words that appear with uniform distribution throughout the corpus and therefore don't mean anything about the statistical model

But when we start out, we want to learn all the topics, and the topic proportions and assignments, but all we have are the documents.

The heavy lifting and machine learning lies in methods to learn topics etc
The inference process is approximate
Mind-boggling that we can take documents and get back all the rest of the information; more mind-boggling that it mostly works

Inference is approximate and randomized so you get a different answer every time
(Not an algorithm, but a heuristic, because it doesn't give the same answer every time)

Topic modeling is a family of statistical techniques for analysing corpora that reperesentes the structure of relationships within and between documents; provides methods for automatically organizing, understanding, searching and summarizing

LDA is the first and most widely used technique; unsupervised clustering of words into topics; foundation for more complex models

(Alternative would be a supervised learning model where you say "here are my categories, please sort things into categories" -- i.e., the things I am accustomed to.)

#### How Do?
* First thing we are going to do: make a bunch of assumptions about the world!
In a fairly rigorous manner, that we can codify statistically

* Then we will organize and collect the data that we will use in the model: gathering all the text files, but also often processing them to simplify/transform files -- e.g., stemming

* Those both allow us to infer the posterior: this is effectively the process of running Mallet; the statistical model in the middle that chugs through the data and then gives an output at the end

* We check & verify that it's good

* We can use it to make predictions (though people only rarely do this) -- I think this is what *I* am interested in doing, using it to see if we can predict whether a work is by a man or a woman. **Are any topics predictive of authorial gender?**

* What we really want to do is explore and understand those topics, and hopefully search for new and meaningful relationships in our dataset

### Things that have been done with topic modelling

Word clouds (weighted by probability) more telling than just lists of each topic's words -- Some topics might have one or two words that dominate the topic, probability-wise, and others have more even distribution: when we talk about brand, we talk about BRAND, but when we talk about justice we talk about a lot of related concepts also

InPhodata topic modelling tool with a useful (though dense) interface: inphodata.cogs.indiana.edu

Andrew Goldstone and Ted Underwood (2012): What can topic models of PMLA teach us about the history of literary scholarship?
Network of interrelated topics, and sparklines of interest in each topic over time

Carson Aievert, Kenneth E Shirley (2014) LDAVis: A Method for Visualizing and Interpreting Documents
http://cpsievert.github.io/LDAVis/reviews/vis/#topic=3&lambda=0.6&term=
Rather than just looking at how strongly associated a word is with a topic, you also have to weight that by how frequently the word appears overall in the corpus -- find the most distinctive/relevant words for each topic
If I'm talking about evolutionary biology, how likely overall is it that I will use the word "biology"? Versus, what words am I only likely to use if I'm talking about evolutionary biology? How salient is the word to the topic?

What's powering all of these different displays is the same data that came out of the same inference data, but doing different things with the final exploration set

#### Q & A

**How many documents is suitable?** ... Once you clear a certain threshold, more texts will allow more fine-grained examination of more topics. (If you do a lot of topics on a more homogenous corpus, the topics are likely to be finer-grained, e.g. archive of PMLA vs archive of just a Victorian studies journal) Determined experimentally! Via guess and check.

Some ways to determine how many topics you can get, some rules of thumb... 100 or more documents at least, of paragraph-to-article length, relatively similar in length. Too short: too little data. Longer than an article: too many different things being talked about for the words that cohere together to find enough signal.

### Lunch conversations

Hung out with Caroline and a friend of hers - mostly talked about the job market, etc, but also touched upon The Field

Something interesting about the forgotten peers of now-famous works (e.g., Ozymandias and Ozymandias) - can I spot the "adjacent possible" which enables a set of similar works? can I draw out why one work ends up being selected for canonization? (e.g. Sherlock Holmes)

### Getting Set Up

Need to have R and RStudio

Create a new project > Version control > Check out a project > Git > paste repository URL

In TopicModelingRTools, run these two commands to make sure all the necessary bits are installed and running properly:
source("functions/lda.R")
source("functions/import.R")

To fix problems with Java, go here: http://charlotte-ngs.github.io/2016/01/MacOsXrJavaProblem.html

in R, run this, making sure to have the right version number in the URL:
dyn.load('/Library/Java/JavaVirtualMachines/jdk1.8.0_**131**.jdk/Contents/Home/jre/lib/server/libjvm.dylib')

the code being used is adapted from Matt Jockers' book -- http://www.matthewjockers.net/books/

Trying to understand how I will be able to do my own topic modelling going forward... do I need to write a .R program that will call mallet and run my LDA? will I be able to, in this R program, easily use structured learning instead?

**LL/token** number tells you how good your model is -- closer to zero is better. e.g., 9.4 with 50 topics and 8.2 with 100 topics: 100-topic model is probably better than 50-topic model. But use with caution! Better metric is actually looking at yout output. If you're getting to 500 runs and you're not seeing improvement in LL/token, no need to run 1000 times -- can stop sooner.

LL is the model's log-likelihood divided by the total number of tokens, this is a measure of how likely the data are given the model. Increasing values mean the model is improving. ([Statistics lesson on likelihood and log-likelihood](https://onlinecourses.science.psu.edu/stat504/node/27))

Got example_1.R running! Got 50 word clouds of topics! They're so pretty! Based on AP news articles -- remarkably coherent topics produced

```> topic.23 <- model$getTopic(23)```
get set up to look deeply at a particular topic

```> topic.23$getWords(10)```
gets the top 10 words predictive of that topic
```> topic.23$getDocs(10)```

gets the documents with the highest proportions of that topic
```> top.docs <- topic.23$getDocs(10)```

make a list of top 10 documents for a topic
```> model$getDocument(names(top.docs[4]))```

gets 4th article in top 10 article list, displays the document itself

### Wrap-up

We've said hello to each other and to R and to topic modelling! Tomorrow we will do a deep dive into 


## June 13 2017
