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

### The statistical model underlying topic modeling!

#### Bayesian statistics review

<!-- I can tell that he really understands what he is talking about, but I am not sure he is explaining it very helpfully... so much of "we all know" and "that makes perfect sense" -->

A function takes in input and returns output; we're going to be working with multi-dimensional vectors with a dimension for every word, so the function will take in thousands of inputs

Easiest probability (function?) is just flipping a coin (a binomial): p(a) -> {H:0.5, T:0.5}

Derivative of a function = area under the curve ```f(x) = ∫f(x)dx```

In computer science, an integral turns into just addition ```Σf'(x)dx```

If it's discrete, everything will add up to one -- the probability that SOMETHING will happen is 100%

Multinomial: a probability distribution function with a lot of different inputs

A document is a series of random draws from a probability distribution function (pool of words) -- with this document, what's the probability that a series of random draws would result in this series of words?

Assuming all words are equally likely, the probability of any one word is ~1/65,000 -- probability of Moby Dick is (1/65k)^200,000 ... seems unlikely that it was random.

But we can also look at the probability of A **and* B occurring together -- ```p(a,b)``` -- what's the probability that it's 95 degrees and June?

```p(a,b) = 1/12 * .01``` as baseline (1/12 months are June, 1% of days in the year are 95 degrees) -- but of course these things influence each other; these variables influence each other

```p(a|b)``` - probability of A **given** B -- called a joint conditional

```p(a,b) = p(a) * p(b|a)``` -- multiplication rule

```p(a,b) = p(b) * p(a|b)```

```p(b|a) * p(a) = p(a|b) * p(b)```

Let's say we're trying to detect cancer! What is the probability that Patient A has cancer, given that some test for cancer is positive? ```p(Cp|T+)```

```p(T+|Cp) * p(Cp) = p(Cp|T+) * p(T+)```

```p(T+|Cp) * p(Cp) / p(T+) = p(Cp|T+)``` -- probability of cancer given positive test will be probability that test is positive when cancer is present times prior likelihood of cancer, divided by prior likelihood of positive test

Positive test means ```p(T+) = 1```

Test is 80% sensitive so ```p(T+|Cp) = .8```

let's say that 1% of people have cancer so ```p(Cp)```

the false positive rate of the test is .008 ```p(Cp|T+)```

A naive Bayesian probability; conditional probabilities are the fundamental structure of Bayesian statistics

#### Time for cartoon models of LDA: The parable of the factory 

Document factory produces some well-defined set of documents (19th
C. novels, Victorian poetry, AP articles, letters of Margaret Sanger)

The process of creating these documents is a trade secret of the
factory that we’d like to reverse engineer to figure out what’s going on

The only evidence we have is the documents that the factory produces
and our theory about what is happening inside

The process of representing our knowledge of what's going on is called supervised learning, and that's a lot of work -- so we're going to use unsupervised learning to make a series of models that are progressively more complex

Maybe inside the factory is a giant bucket of words! And a factory worker goes and scoops some out and dumps them in the document. -- Really easy to figure out what is in the original bucket of words (it's all the words in all the documents and their relative prevalence), but not the most useful model. This makes a word cloud of a whole book, baiscally -- can check basic word frequency, compare ads for girls vs ads for boys for example and see that they use different words

Next most sophisticated model says that there are several different buckets of words to pull from: factory worker first picks a bucket (maybe the whale bucket) and pulls words randomly and that bucket produces Moby Dick, whereas the finches bucket would produce Origin of Species -- more accurate but also more complex; we have to be able to infer how many different buckets there are to calculate the probability of a given document being produced, and we have to guess which bucket the worker went to

Final complication: buckets of buckets! Factory worker scoops 15000 words from bucket 1, scoops 3000 words from bucket 2, 600 words from bucket 3, etc, and then assembles all those words into a document -- now we have to guess which buckets the factory worker picked from, in what proportion he picked from those buckets, and what the contents were of those buckets

Some topics are more popular than others -- those buckets are bigger. (It seems important to me to remember that not all topics are created equal, that it's not actually a flaw in the analysis if some topics predominate or are more/less complex)

**(I feel like the pattern I need to train myself to look for is not "contrast of two things" but "the long tail")**

The buckets totally ignore what order words go in -- built into the model is the assumption that word order doesn't matter. To integrate word order again, try all ngrams (eg 2grams Myname nameis isIshmael) but this MASSIVELY increases necessary of processing

Our model assumes that certains structures are hidden, latent variables that we cannot see and have to infer

The Parable Explained
* Hidden vs. observed structure
* Buckets are probability distributions over a vocabulary
* Documents are multinomials
* Choice of a bucket yields a conditional probability -- ```p(d|b6)``` - what's the probability that I got this bucket given that I went to bucket 6?
* Selection of multiple buckets yields a mixture model  -- this is Blei's insight that documents talk about multiple topics

#### Formalizing our statistical model

[The powerpoint is extremely useful.]()

Two ways to do statistics: evidentialist vs Bayesian. Evidentalist: descriptive, counting all the things that happen. Bayesian: trying to encode belief and uncertainty. Today we're doing Bayesian, but for the most part it doesn't matter

We are inferring and then encoding our beliefs about documents and how they are constructed

David Blei's explanation is actually very readable and useful (my theory: this is part of why he gets cited so much)

Intuition (as we approach topic modelling)
* There are topics
* Words are used differently (i.e., with different frequency) in different topics
* Documents can be about multiple topics

Assumptions (underlying our specific mathematical approach)
* Documents are bags of words -- it is possible to use stemming etc to merge individual words but this usually makes things more confusing
* Topics are fixed and finite -- this is a terrible model of the world!!
* Topics are independent -- also obviously wrong
* Documents are independent -- also obviously wrong!

The generative statistical model behind LDA: the RESULT that topic modelling will produce

The LDA model is expressed as a probability function p. This is the joint probability (or likelihood) of a given set of topics (**β**), a set of per-document topic distributions (**θ**), and the specific association of a topic (**z**) for each word in each document (**w**)

p(β,θ,)

From the outset we willl assume that tere is a universe of K topics, β. We will refer to each individual topic by index *k* as in βk

A topic is formally defined as a probability distribution over a vocabulary *V* (a list of all the words in all the documents) -- words in the vocabulary are terms, words in the document are tokens

Topics are our name for probability distribution functions over a vocabulary -- we can we can and should argue over what a "topic" really is in our model

“We refer to the latent multinomial variables in the LDA model as
topics, so as to exploit text-oriented intuitions, but we make no
epistemological claims regarding these latent variables beyond their
utility in representing probability distributions on sets of words.” – Blei, 2003

We need a way to compute likelihood of any given topic p(βk). To do that we assume that βk is drawn from a Dirichlet. A Dirichlet is a probability distribution function that generates **random** probability distributions. η is a parameter that governs the dispersion of the Dirichlet.

With this universe of topics,we can start generating documents!

For each document d, first, I pick some topics (θd) based on another Dirichlet allocation based on *a*

For each word in that document, choose a topic from θd, then choose a word from that topic's word distribution

(The big boxy diagram that we are working our way through is called plate notation)