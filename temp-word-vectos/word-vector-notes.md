# Word Vectors

"Word vectors actually have an origin going back to the 70s, and word vectors aren't that special" -- essentially my mom's take on them

# 1. Understanding Word Vectors with Visualization

This unit will give a brief introduction of word vectors and word embeddings. Concepts needed to understand the internal mechanics of how they work will also be explained, with the help of plots and visualizations that are commonly used when working with them.

## Setting up
What are these libraries?
* NumPy: This is a package for scientific computing in python. For us, NumPy is useful for vector operations.
* NLTK: Easy to use python package for text processing (lemmatization, tokenization, POS-tagging, etc.)
* matplotlib: Plotting package for visualization
* scikit-learn: Easy to use python package for machine learning algorithms and preprocessing tools
* gensim: Builtin word2vec and other NLP algorithms

### What are word vectors?

A vector is just a list/array of real numbers. A vector has a size/length which indicates how many numbers are in it. In Python you can make a vector using square brackets '[]':
`vector_one = [1, 2, 3]`

A word vector or embedding is a numerical representation of a word within a corpus based on co-occurence with other words. Linguists have found that much of the meaning of a word can be derived from looking at its surrounding context.

## Sparse and dense vectors (SVD, PMI, etc.)

Word vectors (and vectors in general) can be largely classified into sparse and dense vectors.

A sparse vector is count-based vector where each element in the vector represents the integer counts of words, usually co-occurence or frequecy. Because a lot of words don't appear all the time, many elements of sparse vectors are 0, to represent 0 observations.

### Document-term matrix (usually sparse)
One of the simplest and most common ways of constructing a matrix is recording its occurence through out a set of documents. This creates a document-term matrix where one dimension indicates the frequency of a word in documents and the other indicates the vocabulary (all words that occur at least once in your entire corpus). Commonly used in information retrieval; probably won't be used for other kinds of research.

Document-term matrices are mostly used in information retrieval. Drawback of document-term matrices -- weighting by pure frequency is too linear, makes terms less important the more they appear; tf-idf introduces weights. (Is tf-idf... word...... vectors? Yes, I do recall that they are matrices!)


Among the many packages that help you construct your own matrix with your corpus, scikit-learn is one of the most heavily used within the Python scientific stack. Let's import **scikit-learn's CountVectorizer()**

#### scikit-learn's CountVectorizer()

For each word in each document, it will give the count of that word's occurrence in the docs.

A document-term matrix is just a big table (formally, a mathematical matrix) that describes the frequency of words or terms that occur in a collection of documents. In a document-term matrix, rows correspond to documents in the collection and columns correspond to terms.

```
from sklearn.feature_extraction.text import CountVectorizer
documents = [ strings here ]
example_vectorizer = CountVectorizer() #initialize your count vectorizer
example_vectorizer.fit(documents) #documents much be a vector of strings(individual documents)
print("Vocabulary size:", len(example_vectorizer.vocabulary_))
example_vectorizer.vocabulary_  #We can get the unique vocabulary set and its corresponding index here

#  to get all the doc-word counts
counts = example_vectorizer.transform(documents)
print(counts)

# to get counts of individual words in a doc
doc = 0  # first document
for word, word_id in example_vectorizer.vocabulary_.items():
    print(word, ":", counts[doc, word_id])

# to see the matrices themselves
counts = example_vectorizer.transform(documents)
counts.toarray()
```

*The library has a default regex setting which removes single-character words like "a" and "I"!* 1-letter words are being ignored. That's due to the way CountVectorizer() splits sentences into words. CountVectorizer() has options to customize this behaviour and it allows to specify your own regular expression to extract words, disregard stopwords, count ngrams instead of words, cap the max number of words to count, normalize spelling, or count terms within a frequency range. It is worth exploring the documentation: http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html

To include single-character letters instead, use a new regex:

```
new_regex = r"(?u)\b\w+\b"  # this regex now considers single character tokens
CountVectorizer(token_pattern=new_regex).fit(documents).vocabulary_
```

So, another way to get the array:

```
new_regex = r"(?u)\b\w+\b"  # this regex now considers single character tokens
CountVectorizer(token_pattern=new_regex).fit(documents).vocabulary_

my_corpus = ['wow this is the best workshop ever','test document here','time to add another document''this workshop should be given every year','i wonder if other people feel the same']
my_vectorizer = CountVectorizer()
my_vectorizer.fit(my_corpus) 
my_vectorizer.transform(my_corpus).toarray()
```

To see the vocabulary (words and their IDs):

```
print("Vocabulary size:", len(lit_vectorizer.vocabulary_))
lit_vectorizer.vocabulary_
```

To just see a list of all the words, without their IDs, alphebetized:

```
# You can look up all the words in the vocab from the three novels
lit_vectorizer.get_feature_names() 

To get the ID of a given vocab term:

```
print("The ID of the word 'piece' is ", str(lit_vectorizer.vocabulary_.get('piece')))
```

```

An even shorter way to get the document matrix:

```
X = my_vectorizer.fit_transform(corpus)
X = X.toarray()
```

Another kind of info to get about the matrix: ```X.shape # How many novels are there?   # How big is our vocabulary?``` -- returns two numbers, number of docs and number of vocab terms

```
print("The doc-term matrix has {} documents and {} dimensions.".format(str(X.shape[0]), str(X.shape[1])))
```

#### Can also treat each sentence as a document

```
from nltk import sent_tokenize
sentences = []
for novel in ['melville-moby_dick.txt', 'austen-emma.txt', 'edgeworth-parents.txt']:
    sentences += sent_tokenize(gutenberg.raw(novel))

lit_vectorizer = CountVectorizer(token_pattern=new_regex)
X = lit_vectorizer.fit_transform(sentences).toarray()
X.shape

print('There are '+str(len(X[:,8860]))+' total elements since there were this many sentneces total')
print("... and of these " + str(len(np.where(X[:,8860]>0)[0])) + " have non-zero entries.")
#What does that mean about this word?
print("In total this word appears " + str(np.sum(X[:,8860])) + " times.")
#What does that say about this word?
```

### Word-word matrices

In the previous section we looked at representing words by their relations to a corpus of documents. What about their relation to one another? The most intuitive way of doing this is to build a word-word matrix where now both dimensions are the vocab and each element at [k][l] represents the co-occurence of the vocab k with vocab l in a window of w. The window of w indicates the number of words before and after given word k where we count occurrences of l. w is usually around 4. (Always produces a symmetrical matrix because it is just co-occurrence and not order.)

Again there is a simple library!

```from nltk.tokenize import word_tokenize```

```
import coocc #look for this file in our directory

a = ['a c b c b c a d d a c c a d c b a d c'] #the corpus

v, m = coocc.ww_matrix(a, word_tokenize, 2) #This is not the most efficient function, sorry
# it takes in the corpus, the function word_tokenize, and the window size

m.toarray(), v
```

Using a text:

```
#Doing this for mobydick
mobydick = gutenberg.raw('melville-moby_dick.txt')
v, m = coocc.ww_matrix([mobydick], word_tokenize, 4) 
X = m.toarray()
X
X.shape
```

Looking at specific workds:

```
#Now, say we want to the word vectors for 'happy','sad','angry' again
#We need to first get the indices
happy_i = v['happy']
sad_i = v['sad']
angry_i = v['angry']

happy_ww = X[happy_i,:]
sad_ww = X[sad_i,:]
angry_ww = X[angry_i,:]
np.set_printoptions(threshold=np.inf)
happy_ww  #looking at this vector for happy... 
```

Investigating specific co-occurences:

```
#You can look up the co-occurrence of two words within a window
#How many times does dark occur with night in a window of 4?

dark_i = v['dark']
stormy_i = v['stormy']
night_i = v['night']

X[night_i][dark_i]
```

### PPMI Matrix

[Not discussed during the workshop - a way to weight matrices to be less linear]

If we look at our word-word matrix, you'll see that because it is only recording the raw co-occurrences, it makes no adjustments for how certain words are just more frequent. For instance, words such as 'is' or 'the' are more likely to appear together with any other word w than other words. Pointwise mutual information introduces a weighting scheme to take into account co-occurence relative to two words' independent freqencies.

Since these methods are tricks/engineering to improve results and there is no absolute truth to what is the best method. Here is one for  ww  as target word and  cc  as the context word:

PPMIα(w,c)=max(log2P(w,c)P(w)Pα(c))
PPMIα(w,c)=max(log2P(w,c)P(w)Pα(c))
 
Pα(c)=count(c)α∑ccount(c)α
Pα(c)=count(c)α∑ccount(c)α
 
Notice the PPMI is taking the log ratio of the probability of co-occurrence over the probability of individual freqencies. We only consider positive value because negative probabilties (when the co-occurence is lower than expected) fluctuate. The \alpha is a measure correct for rare words with high PMI.

*PPMI: Positive Pointwise Mutual Information

Levy, O., Goldberg, Y., and Dagan, I. (2015). http://www.aclweb.org/anthology/Q15-1016

## Dense Vectorization

We have so far looked at vectorization methods where each element correspondence to a discrete entity such as a term from the vocabulary or a document. We have seen that this results in a lot of 0 entries, making the matrices sparse.

Dense vectors have become more popularized lately due to deep-learning based vectors such as GloVe and Word2Vec. We will examine the truncated SVD, one dense vectorization method that is not deep-learning based but used widely.

### SVD

Singular Value Decomposition (SVD) is a common method (using linear algebra) for identifying dimensions with highest variance. It is a form of dimension reduction where the algorithm identifies ways of condense as much of the information of the data in with fewer dimensions. SVD factorizes a given matrix  XX  into three matrices:

SVD(X)=WΣCT
SVD(X)=WΣCT
 
where X is a word-word matrix,  WW  is a matrix of your new dense vectors, and  ΣΣ  is a row of singular values that represent the importance (how much variance encoded) the corresponding dimension is. Starting from the top, the first dimension encodes the most information and the following dimensions are orthogonal the the previous and contain less information down the line. A truncated SVD is the same thing but taking only  kk  top dimensions.

(CT is a context vector that you may not need; WW, the matrix, is the crucial part)

See here for more information: https://web.stanford.edu/~jurafsky/slp3/16.pdf

Σ = Eigenvalues (on the diagonal..?) that show which dimensions are most important; these let you focus on fewer dimensions.

SVD reshapes the matrix to choose to the top most relevant dimensions (i.e., the ones that encode the most variance in the data). This is why it's called TruncadedSVD -- it truncates the matrix. It's basically PCA.

The first dimension will chosen to be orthogonal to the second dimension, and so on for however many dimensions chosen. (2 is common because then we can look at it.)

"Thanks to our ancestors, we can use code that they wrote for us"

```
# You can do this super easily with sklearn!
from sklearn.decomposition import TruncatedSVD
svd = TruncatedSVD(n_components=8) #this is your K (how many top dimensions you want to keep)

denseX = svd.fit_transform(X) #n_samples, n_dims

#What is the shape of this matrix?
denseX.shape
```

Looking individual words:
```
happy_vector_dense = denseX[v['happy'],:]
sad_vector_dense = denseX[v['sad'],:]
angry_vector_dense = denseX[v['angry'],:]

happy_vector_dense # the dense version

happy_ww # the sparse version
```

"Why are these floats?" "Because it's linear algebra magic... We're not doing counts any more. They're not probabilities. The most important thing is that these floats are related with other floats."

*CAN'T compare the vectors from one SVD to another SVD, because these floats are only meaningful in relationship to the floats from the **same matrix**.*

It IS deterministic, so if you use the same corpus you will get the same exact vectors every time!! Unlike Word2Vec / deep learning.

## Vector Usages

There are several ways of working with vectors and the most useful for our purposes may be similarity. We will explore this further in the next section as well.

There are several ways to measure distance between two vectors. The most widely used is cosine similarity. This a cosine measure of angle between two vectors. Mathematically, cosine similarity looks like this:

cos(v⃗ ,w⃗ )=dot(v⃗ ,w⃗ )norm(v⃗ )norm(w⃗ )
cos(v→,w→)=dot(v→,w→)norm(v→)norm(w→)
dot(v⃗ ,w⃗ )=∑i=0nviwi
dot(v→,w→)=∑i=0nviwi
norm(v⃗ )=∑i=0nv2i⎯⎯⎯⎯⎯⎯⎯⎯⎯
norm(v→)=∑i=0nvi2
We normalize here because we want to normalize out frequency so that word similarity disregards frequency.

Cosine similarity will range from 1 to -1. Closer to 1 means closer in direction, closer to -1 opposite in direction and something close to 0 means orthogonal.

```
from sklearn.metrics.pairwise import cosine_similarity 

# So that we can see more contrast when evaluating similarity, let's add in a rather different word: 'biscuit'

index = v['elated']
elated_vector_dense = denseX[index,:]

happy_vector = happy_vector_dense.reshape(1,-1) 
sad_vector = sad_vector_dense.reshape(1,-1)
angry_vector = angry_vector_dense.reshape(1,-1)
elated_vector = elated_vector_dense.reshape(1,-1)

#angle between happy and sad
cosine_similarity(happy_vector, sad_vector)

cosine_similarity(angry_vector, sad_vector)

cosine_similarity(happy_vector, angry_vector)

cosine_similarity(happy_vector, elated_vector)
```

When testing the comparisons of emotional vectors, they all came back as basically the same, because she had earlier reduced to only 2 components -- lost too much data. Even with more data, happy and sad are more similar than sad/angry or happy/angry... but this is very arbitrary because our corpus is so small (just Moby Dick)

### K-means clustering

K-means is an iterative algorithm that finds clusters of similar vectors by first assigning observations to their nearest means (initially randomly chosen) as its cluster and then calculating the new centroids of these clusters.

It is called k-means because you are splitting all of your observations into k clusters by their means.

K-means is an iterative algorithm that finds clusters of similar vectors by first assigning observations to their nearest means (initially randomly chosen) as its cluster and then calculating the new centroids of these clusters. It iterates until it finds something optimal.

It is called k-means because you are splitting all of your observations into k clusters by their means.

```
from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=3)

np.set_printoptions(threshold=20)
predictions = kmeans.fit_predict(select_matrix)
predictions
```

## Visualization

### t-sne visualization

You have probably heard of **t-sne** (is it TEA SNEA? or TAE SNAE..)!  This is "newer" dimension reduction method that emphasizes visual convenience. Sometimes PCA can produce overlapping/crowding of similar points but tsne will rearrange them. The con of tsne is that it is not as easily interpretable as PCA. It's also non-deterministic -- you'll get different but similar results every time. But we thought you should play with it here since it has been widely used in machine learning today.

```
from sklearn.manifold import TSNE
tsne = TSNE(n_components=2) #n-components = reduced dimensions

#Let's make a matrix of random words
random_indices = np.random.choice(len(v), 100, replace=False)
select_matrix = X[random_indices]
lookup = {val:key for key,val in v.items()}
labels = [lookup[w] for w in random_indices]

select_matrix.shape

labels # print all the words

embed = tsne.fit_transform(select_matrix)

embed
```

To plot 100 random words:
```
random_x, random_y = zip(*embed)
fig, ax = plt.subplots(figsize=(16, 8))
ax.scatter(random_x, random_y, alpha=.8)

for _, lab in enumerate(labels):
    ax.annotate(lab, (random_x[_]+.1, random_y[_]-.05))

plt.title("random 100 embeddings")
plt.show()
```

To visualize the clustering (of 100 words), with each cluster a different color:

predictions = kmeans.fit_predict(select_matrix)

```
first_cluster = np.array(embed[np.where(predictions == 0)])
second_cluster = np.array(embed[np.where(predictions == 1)])
third_cluster = np.array(embed[np.where(predictions == 2)])
```

To do it to Moby Dick:

```
n_clusters = 15
kmeans = KMeans(n_clusters=n_clusters)
predictions = kmeans.fit_predict(denseX)
tsne = TSNE(n_components=2)

embed = tsne.fit_transform(denseX)
random_x, random_y = zip(*embed)

plt.figure(figsize=(16, 8), dpi=80)
plt.scatter(random_x, random_y, alpha=0.3)
plt.title("tsne visual of all " +str(len(v)) + " word embeddings")
```

**Recommended size: at least a few billion tokens.** Though it depends on the research Qs; document classification might be able to train on a smaller corpus and still get good results from smaller vectors. But rich embedding of semantic content needs larger corpus. Also depends on the size of vocabulary: if the vocabulary is smaller might need fewer tokens.

What are the limitations of these word vectors?
What are the different use cases between count-based vectors and word2vec? (size of corpus)
What are limitations?
Why do we use Word2Vec instead?

# 2. Word Vectors via Word2Vec
This unit will focus on Word2Vec as an example of neural net-based approaches of vector encodings, starting with a conceptual overview of the algorithm itself and ending with an activity to train participants’ own vectors.

## Conceptual explanation of Word2Vec

OK, before we go into Word2Vec in practice, let's talk about what it is.

Word2Vec is a neural-network or deep learning based approach of generating word vectors. There are many resources out there that will go into the heavy details of deep learning in general or deep learning for NLP such as Yoav Goldberg's Neural Network Methods in Natural Language Processing (Morgan & Claypool Publishers, 2017). In this unit, we will give you a high level overview -- just enough for you to understand what w2v really means.

Neural nets are basically a bunch of weights in the form of matrices. If you have lots of these matrices multiplies in a row, you get layers that make your network 'deep' - hence the name deep learning. Usually if your network has one hidden (or projection) it's called a 'deep' network. The 'neurons' are just functions that transform your data non-linearly. Each layer of the network will tranform your data so your weights become more sophisticated (and meaningful?) with each layer.

What happens in all deep learning tasks is a prediction of some sort. In the case of word2vec, we predict words, given other words. The information for making this prediction is in your weights -- matrices. Based on whether this prediction is correct, the model will calculate the cost and alter your weights, matrices, so that you can do better on the next prediction. This is done iteratively through all of your 'training' data.

In W2V, your actual predictions are not the end-

The main difference between skip-gram and CBOW, two different methods of w2v, is that while skip gram learns vectors by predicting the context words that come before and after our given word  ww , CBOW predicts the center word  ww  given context words

You may have heard of negative sampling. This is just a short-cut for calculating the denominator needed for the probabilities. Because it turns out to be costly to calculate the denominator exactly everytime, negative sampling approximates the ratio by taking samples of random words from a uniform distribution.

### The short version:
Two ways to do W2C: either try to predict what the context words around a word will be (a skip-gram), or try to predict the middle word given the context words (CBOW, Continuous Bag of Words, standard NLP). Predicts based on Every time it makes a prediction, it gets a "cost" (machine learning works like this) and it tries to minimize its costs, by back-propagating all the weights in the model so that the next time it sees a similar context it will be more likely to guess the thing it saw before.

## Using Word2Vec

Will use gensim, which is highly trainable. Need to reformat corpus into sentences for gensim.

### Training our own vectors

```
from nltk.corpus import gutenberg

mobydick = gutenberg.raw('melville-moby_dick.txt')
emma = gutenberg.raw('austen-emma.txt')
parents = gutenberg.raw('edgeworth-parents.txt')

corpus = [mobydick, emma, parents]

sentences = sent_tokenize(corpus[0])
sentences

tokenizer = TreebankWordTokenizer()

# sentences = [['hi', 'there'], ['this', 'is', 'a', 'sentence']]
# ^ the only format gensim likes 

def make_sentences(list_txt):

    all_txt = []
    for txt in list_txt:
        lower_txt = txt.lower()
        sentences = sent_tokenize(lower_txt)
        sentences = [tokenizer.tokenize(sent) for sent in sentences]
        all_txt += sentences
        print(len(sentences))  # let's check how many sentences there are per item
    return all_txt
    
sentences = make_sentences(corpus)
```

### Parameters!!
To train our vectors we call this function below. This function has a couple dozen parameters, some of which are more important than others. We will explain a few major parameters here. The fields that are MANDATORY are marked with an asterisk:

1. ```sentences*```: This is where you provide your data. It must be in a format of iterable of iterables.
1. ```sg```: Your choice of training algorithm. There are two standard ways of training W2V vectors -- 'skipgram' and 'CBOW'. If you enter 1 here the skip-gram is applied; otherwise, the default is CBOW.
1. ```size*```: This is the length of your resulting word vectors. If you have a large corpus (>few billion tokens) you can go up to 100-300 dimensions. Generally word vectors with more dimensions give better results.
1. ```window```: This is the window of context words you are training on. In other words, how many words come before and after your given word. A good number is 4 here but this can vary depending on what you are interested in. For instance, if you are more interested in embeddings that embody semantic meaning, smaller window sizes work better.
1. ```alpha```: The learning rate of your model. If you are interested in machine learning experimentation with your vectors you may experiment with this parameter. How fast you update the weights.
1. ```seed (int)```: This is the random seed for your random initialization. All deep learning models initialize the weights with random floats before training. This is a useful field if you want to replicate your experiments because giving this a seed will initialize 'randomly' deterministically.
1. ```min_count```: This is the minimum frequency threshold. If a given word appears with lower frequency than provided it will be ignored. This is here because words with very low frequency are hard to train.
1. ```iter```: This is the number of iterations (entire run) over the corpus, also known as epochs. Usually anything between 1-10 is ok. The trade offs are that if you have higher iterations, it will take longer to train and the model may overfit on your dataset. However, longer training will allow your vectors to perform better on tasks relevant to your dataset.

Overall, most of these settings wil not concern you unless you are interested in very specific usages of word vectors.

Again the question is: **how small can my corpus be?** -- can overfit on purpose...? Microgenres project at the LitLab is interested in how small overfitted characteristics show in a larger corpus.

Train the model:

```
model_example = gensim.models.Word2Vec(sentences, min_count=1, size=100)
```

Another way to train the model is to use the LineSentence function
```
# provide the name of the corpus text you want to train on
linesentence_example = gensim.models.word2vec.LineSentence('text8')

model = gensim.models.Word2Vec(linesentence_example, min_count=1, size=100)

model.wv.vocab
```

To save the trained model (often necessary for large ones!):
```
model.save('our_model')
```

To load it:
```
our_model = gensim.models.Word2Vec.load('our_model') 
```
Given the size of word2vec models, we'll often load just the vectors into memory, and delete the full model to save RAM.

```
my_model = our_model.wv 

del our_model 

print(type(my_model))
```

**Even though Word2Vec is carrying out a prediction task, we're not interested in the predictions itself -- we're interested in the side project, ie the weights.**

### Pre-trained vectors

Might be useful if your own corpus isn't very big. Trained on things like Twitter and Google News.

With deep learning, more data is always better. The scale is completely different from other kinds of machine learning.

"Transferred learning": pre-trained vectors are train for days or weeks; no way for an independent researcher can train for weeks, so you can jump-start by taking the pre-existing and train on top of it. But if the corpus is small it's a drop in the bucket, may not be able to see the effect.. may be able to tweak/engineer it by adjusting the alpha rate...

Also depends on the corpus you're transferring from. You're transferring the relational stuff, the relationships between words -- so can't use Twitter training to examine 17thC texts. Have to think critically about whether you're using the right kind of vector for you question; might be able to use a different vector (like tf-idf) that has different reliability.

Word vectors tied to collocation/condordances -- the advantages are scale.

```
import gensim.downloader as pretrained
pretrained.info('text8')
news_model = pretrained.load('word2vec-google-news-300')
my_model = news_model.wv
```

Given these vectors, let's explore some similarity tasks.

```
my_model.similarity('beautiful','sublime')  # Using Cosine-similarity

from sklearn.metrics.pairwise import cosine_similarity
cosine_similarity(my_model['beautiful'].reshape(1,-1), my_model['sublime'].reshape(1,-1))
```

Gensim gives us a number of handy methods, such as this one that returns a list of most similar words to a given word.

```
my_model.most_similar('democracy'), my_model.most_similar('liberalism')

my_model.most_similar('pluralism', topn=20)
```

Turns up words like "democratic" and "democracies" because these will appear in similar contexts.

Given a list of words, we can identify the most similar word to one we provide.
```
candidates = ['sweet','sour','bitter','nice']
my_model.most_similar_to_given('blueberry', candidates)

for c in candidates:
    print(c, my_model.similarity('blueberry',c))
```

If we want to a list of words that are closer to a given word than some other word of interest, there's an easy method for it. You could read the below as, "words closer to cold than is the word dry".

```
my_model.words_closer_than('cold','dry')
```
You can also play with analogy tasks. The commonly seen task is:

'London is to England as Baghdad is to ____?'

' A is to A*. as B is to B* '

Gensim provides two different ways of implementing this task. You may be more familiar with the the additive version also called the 3CosAdd method:

arg maxb∗∈V(cos(b∗,b)−cos(b∗,a)+cos(b∗,a∗))
arg maxb∗∈V(cos(b∗,b)−cos(b∗,a)+cos(b∗,a∗))
 
This reflects the abstraction of Baghdad - London + England. In this maximization, we are searching which word vector will allow us to produce the highest value in this equation.

The second is a more balanced approach proposed by Levy & Goldberg 2014 (http://www.aclweb.org/anthology/W14-1618)

We find B by going through all of the possible B in the set of vocabulary (V) and identifying which returns the highest value. In other words, finding the argument that maximizes the following equation where the epsilon is added only to avoid division by zero. This is also called the 3CosMul method:

arg maxb∗∈Vcos(b∗,b)cos(b∗,a∗)cos(b∗,a)+ϵ
arg maxb∗∈Vcos(b∗,b)cos(b∗,a∗)cos(b∗,a)+ϵ
 
We can implement this method with a provided function. Positive here refers to words that give the positive contribution to similarity (nominator), and negative refers to words that contribute negatively (denominatory).

Here's the additive method.

```
my_model.most_similar(positive=['woman','king'], negative=['man'])
```

Here's the multiplicative method.

```
my_model.most_similar_cosmul(positive=['england','baghdad'], negative=['london'])
#This is not correct! Gives the wrong capital. Why?
```

Unfortunately in this example we see that this returns Afganistan (when Baghdad is the capital of Iraq!). This is an example of how the corpus can bias our findings.

We know enough to start asking some questions. What are good vectors? What are bad vectors? How much training/data do we need?

Consider this. What would happen if you retrained your model on the same corpus? Would you get the same vectors?

Gensim has quite a few built-in tools, and it's worth taking some time to see what's available. Check the documentation here: https://radimrehurek.com/gensim/models/keyedvectors.html

## GloVe vectors rather than W2V vectors with gensim

GloVe predicts ratios of co-occurrence without using sliding window, so it's faster to train -- no for-loop going throught the whole corpus. But because you need the whole matrix before you start training, you can't train on top of it / add to it after you train. (Whereas Word2Vec you can just keep re-training because it's like the text got longer; the sliding window just keeps sliding

If you've been reading about word vectors, you may have heard about GloVe vectors. Gensim can work with those too! Let's take a look at GloVe vectors so that we can understand the difference and see how to use them in Gensim.

How are Glove and W2V different?

GloVe is also a deep learning based approach and trains in similar ways. The main difference is that GloVe predicts the ratios of co-occurrence, such as the elements your saw in the PMI matrix in part 1. GloVe doesn't have a sliding window as does W2V, it constructs a co-occurrence matrix before-hand instead. This is why sometimes GloVe is faster but W2V have be continuously trained with new data whereas GloVe must be trained from scratch everything (construct a new matrix everytime)..)

But Word2Vec does do better at most tasks... GloVe code just in case:

```
from gensim.scripts.glove2word2vec import glove2word2vec
from gensim.models import KeyedVectors
glove_file = "./glove.6B/glove.6B.300d.txt"
glove2word2vec_file = "glove2word2vec.txt"
glove2word2vec(glove_file, glove2word2vec_file) #we simply call this function to reformat it a bit
glove_model = KeyedVectors.load_word2vec_format(glove2word2vec_file, binary=False) #read in the same file 
```

Given the same test with England and Baghdad from above, let's see how GloVe does. 

```
Given the same test with England and Baghdad from above, let's see how GloVe does. 
```

## PCA visualization

Principal Component Analysis is way of analying your data's principal components! Like SVD from part 1, PCA returns dimensions in order of representing highest variance of your data.

Making the matrices:

```
import numpy as np
from sklearn.decomposition import PCA

countries = ["china", "russia", "france", "germany","greece","japan","italy"]

capitals = ["beijing","moscow","paris","berlin","athens","tokyo","rome"]

X = []
​
for loc in countries+capitals:
    X.append(glove_model[loc])

pca = PCA(n_components=2)
xy_coords = pca.fit_transform(X)
loc_x, loc_y = zip(*xy_coords)

loc_x
```

Visualizing:
```
%matplotlib inline
import matplotlib.pyplot as plt


fig, ax = plt.subplots(figsize=(16, 8))
ax.scatter(loc_x, loc_y)

for _, location in enumerate(countries+capitals):
    ax.annotate(location, (loc_x[_]+.05, loc_y[_]-.05))

plt.title("Countries and their Capitals")
plt.show()
```

# 3. Pre-trained Models and Extended Vector Algorithms
This unit will explore the various flavors of word embeddings specifically tailored to sentences, word meaning, paragraph, or entire documents. We will give an overview of pre-trained embeddings, including where they can be found and how to use them.

## Setting up

What are these libraries?
* NumPy: This is a package for scientific computing in python. For us, NumPy is useful for vector operations.
* NLTK: Easy to use python package for text processing (lemmatization, tokenization, POS-tagging, etc.)
* gensim: Built-in word2vec and other NLP algorithms
* fastText: Super fast word embeddings library

## Out-of-vocabulary words and pre-trained embeddings

Out-of-vocabulary words: matrices made by Word2Ved and GloVe can't give any information on words that are not already in the corpora; they fail

This is known as the Out-Of-Vocabulary (OOV) issue in Word2Vec and similar approaches.

Now, you may think, I could get synonyms of the OOV words using something like WordNet, and then look for those words' embeddings. And while that might work in some cases, in others it is not that simple. Two such cases are new-ish words like facebook and google, or proper names of places, like Teotihuacan.

One way to solve this issue is to use a different measure of atomicity in your algorithm. In Word2Vec-like approaches, including GloVe, the word is the minimum unit, and as such, when looking for words that are not in the vocabulary there is certainly no vector information for it.

In contrast, a different approach could train for sub-word units, for example 3-grams of characters. While not guaranteeing that all words will be covered, a good amount of them might be, due to the fact that it's more likely for all possible trigrams to be included in a large enough corpus than all possible words. This is the approach taken by Facebook's fastText.

**Why... do we assume... that a trigram of characters........ means anything?

fastText gives us a word vector for "google" in Alice in Wonderland, but that... seems like........... an error????? It shouldn't do that??????????????**

fastText also distributes word vectors pre-trained on Common Crawl and Wikipedia for more than 157 languages. These models were trained using CBOW with position-weights, in dimension 300, with character n-grams of length 5, a window of size 5 and 10 negatives. They come in binary and text format: binary includes a model ready to use while the text format only contains the actual vectors associated to each word on the training set.

### Gensim FastText

Gensim is soon to include a special method to load in these fasText embeddings (not working as of 3.4.0). Just take into account that only the .bin format allows for OOV word vectors. For the regular and usually lighter .vec format you still would need to load in the vectors, save a binary Gensim model, and load it back in.

Let's see a couple of examples of using .vec from the Somali and the Simplified English Wikipedia corpora available for fastText. These files are loaded in using the regular Gensim KeyedVectors word2vec model (.load_word2vec_format()), and vectors for out of vocabulary cannot be computed.

In Somali, the word xiddigta (meaning the star) should have its own vector avalilable since the word is present in the corpus.

But the word ciyaalsuuq (meaning unruly youth) raises a KeyError in the word vectors dictionary.

And the same thing occurs in English: while words like star are certainly available, words such as bibliopole (meaning a person who buys and sells books, especially rare ones) are not.

The fastText English embeddings *without* sub-word information are also included in Gensim's downloader feature.

By contrast, when using the .bin file and loading it in Gensim using the special Fastext.load_fasttext_format() method, out of vocabulary words suddenly have embeddings available.

As we've seen, non-existing words in English, such as the Somali ciyaalsuuq, also become available, so it's a feature we must be very careful when using.

In other words, since it gives an answer for words that don't exist, it also gives an answer for words that don't exist.

Semantic information doesn't really hold. If you look for the most similar words to ciyaalsuuq, it gives nonsense. (Or, well, other words that are transliterated from other languages.)

It works sometimes because it can respond to morphologial details of the words, but there's no way to guarantee that you're using good vectors. It's commonly used for machine translation.

What method is being used to make the vectors: a neural net with skipgram

### python fastText package
While Gensim provides a way to create fastText embeddings with sub-word information and even load fastText pre-trained word embeddings, there is also a standalone tool, fasttext, and an accompanying Python library to do the same. Unfortunately, the Python bindings haven't been updated and it seems to be broken when trying to load in binary models generated with newer versions of the fastText command line tool.

```
import fasttext

try:
    fasttext.load_model("wiki.simple.bin")
except Exception as e:
    print(e)

fasttext.skipgram(nltk.corpus.gutenberg.abspath('carroll-alice.txt'), 'alice_model')

fasttext.cbow(nltk.corpus.gutenberg.abspath('carroll-alice.txt'), 'alice_model')
```

Setting up text for seniment analysis:

```
text = """
__label__pos This is some wonderful positive text.
__label__neg This is some awful negative text.
"""
with open('sentiment_train.txt', 'w') as f:
    f.write(text.strip())
test = """
__label__pos This is wonderful.
__label__neg This is awful.
"""
```

Training a classifier, in this case sentiment:

```
with open('sentiment_test.txt', 'w') as f:
    f.write(test.strip())

classifier = fasttext.supervised('sentiment_train.txt', 'sentiment_model')
result = classifier.test('sentiment_test.txt')
print('Precision:', result.precision)
print('Recall:', result.recall)
print('Number of examples:', result.nexamples)
print('"This is wonderfully awful":',
      classifier.predict_proba(['This is wonderfully awful'])[0][0])
```

If you test on the same data you train on, you are in danger of overfitting

## FastText generally

It traisn very very fast, and it can be restrained

## Pre-trained vectors

The list of pre-trained word vectors grows every day, and while it's impractical to enumerate them all, some of them are listed below.

- English
  - fastText. Embeddings (300 dimensions) by Facebook [with](https://s3-us-west-1.amazonaws.com/fasttext-vectors/wiki-news-300d-1M-subword.vec.zip) and [without sub-word information](https://s3-us-west-1.amazonaws.com/fasttext-vectors/wiki-news-300d-1M.vec.zip) trained on Wikipedia 2017, UMBC webbase corpus and statmt.org news dataset (16B tokens), and on [Common Crawl (600B tokens)](https://s3-us-west-1.amazonaws.com/fasttext-vectors/crawl-300d-2M.vec.zip).
  - [Google News](https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/). Embeddings (300 dimensions) by Google trained on Google News (100B) using word2vec with negative sampling and context window BoW with size ~5 ([link](http://code.google.com/p/word2vec/)). There also fastText versions from 2016 with and without sub-word information for Wikipedia and with no sub-word information for Common Crawl.
  - [LexVec](https://github.com/alexandres/lexvec). Embeddings (300 dimensions) trained using LexVec with and without sub-word information trained on Common Crawl, and on Wikipedia 2015 + NewsCrawl.
  - Freebase [IDs](https://docs.google.com/file/d/0B7XkCwpI5KDYaDBDQm1tZGNDRHc/edit?usp=sharing) and [names](https://docs.google.com/file/d/0B7XkCwpI5KDYeFdmcVltWkhtbmM/edit?usp=sharing). Embeddings (1000 dimensions) by Google trained on Gooogle News (100B) using word2vec, skip-gram and context window BoW with size ~10 ([link](http://code.google.com/p/word2vec/)).
  - [Wikipedia 2014 + Gigaword 5](http://nlp.stanford.edu/data/glove.6B.zip). Embeddings (50, 100, 200, and 300 dimensions) by GloVe trained on Wikipedia data from 2014 and newswire data from the mid 1990s through 2011 using GloVe with AdaGrad and context window 10+10 ([link](http://nlp.stanford.edu/projects/glove/)).
  - Common Crawl [42B](http://nlp.stanford.edu/data/glove.42B.300d.zip) and [840B](http://nlp.stanford.edu/data/glove.840B.300d.zip). Embeddings (300 dimensions) by GloVe trained on Common Crawl (42B and 840B) using GloVe and AdaGrad ([link](http://nlp.stanford.edu/projects/glove/)).
  - [Twitter (2B Tweets)](http://www-nlp.stanford.edu/data/glove.twitter.27B.zip). Embeddings (25, 50, 100, and 200 dimensions) by GloVe trained on Twitter (27B) using GloVe with GloVe and AdaGrad ([link](http://nlp.stanford.edu/projects/glove/)).
  - [Wikipedia dependency](http://u.cs.biu.ac.il/~yogo/data/syntemb/deps.words.bz2). Embeddings (300 dimensions) by Levy & Goldberg trained on Wikipedia 2015 using word2vec modified with word2vec and context window syntactic dependencies ([link](https://levyomer.wordpress.com/2014/04/25/dependency-based-word-embeddings/)).
  - [DBPedia vectors (wiki2vec)](https://github.com/idio/wiki2vec/raw/master/torrents/enwiki-gensim-word2vec-1000-nostem-10cbow.torrent). Embeddings (1000 dimensions) by Idio trained on Wikipedia 2013 using word2vec with word2vec, skip-gram and context window BoW, 10 ([link](https://github.com/idio/wiki2vec#prebuilt-models)).
  - [60 Wikipedia embeddings with 4 kinds of context](http://vsmlib.readthedocs.io/en/latest/tutorial/getting_vectors.html#). Embeddings (25, 50, 100, 250, and 500 dimensions) by Li, Liu et al. trained on Wikipedia using Skip-Gram, CBOW, GloVe with original and modified and context window 2 ([link](http://vsmlib.readthedocs.io/en/latest/tutorial/getting_vectors.html#)).
- Multi-lingual
  - [fastText](https://fasttext.cc/docs/en/crawl-vectors.html). Embeddigns for 157 languages trained using fastText on Wikipedia 2016 and Common Crawl using CBOW with position-weights, 300 dimensions, with character n-grams of length 5, a window of size 5 and 10 negatives. Both vectors and binary models for OOV are available. There is an old version of these embeddings trained only on Wikipedia 2016 for almost [300 languages](https://fasttext.cc/docs/en/pretrained-vectors.html).
  - [BPEemb](https://github.com/bheinzerling/bpemb). Pre-trained subword embeddings in 275 languages, based on Byte-Pair Encoding (BPE) on Wikipedia 2017 with sub-word information.
  - [Kyubyong's wordvectors](https://github.com/Kyubyong/wordvectors#pre-trained-models). Embeddings with and without sub-word information trained on Wikipedia dumps from 2017 for +30 languages.
  - [Polyglot](https://sites.google.com/site/rmyeid/projects/polyglot#h.p_ID_98). Embeddings for more than 100 languages trained on their Wikipedias from 2013. Provides competitive performance with near state-of-art methods in English, Danish and Swedish.

There is even a library, [`chakin`](https://github.com/chakki-works/chakin#supported-vectors), that allows to easily download word vectors with and without sub-word information for 11 languages.

### Historical word vectors

In the Humanities, despite the value of word embeddings, we usually want to train our own models or to have access to models that are related to a specific time period of study. It might not be of much help to analyze 19th Century literature with word vectors trained on a Google News corpus, specially since the semantic of the words themselves have been proven to change over time.

There is, however, a collection of [historical word vectors](https://nlp.stanford.edu/projects/histwords/) made avaliable to use by the Stanford NLP Group and others (special thanks to [Ryan Heuser](http://ryanheuser.org/)). The embeddings (300 dimensions) are generated using word2vec skip-gram with negative sampling and trained on Google N-Grams for English, English Fiction, French, German, and Simplified Chinese; on the Corpus of Historical American English (COHA); and on the Century Collections Online (ECCO):
- English:
  - [All English](http://snap.stanford.edu/historical_embeddings/eng-all_sgns.zip) (1800s-1990s by decade)
  - [English Fiction](http://snap.stanford.edu/historical_embeddings/eng-fiction-all_sgns.zip) (1800s-1990s by decade)
  - [Genre-Balanced American English](http://snap.stanford.edu/historical_embeddings/coha-word_sgns.zip) (1830s-2000s by decade) (COHA)
  - [Genre-Balanced American English, word lemmas](http://snap.stanford.edu/historical_embeddings/coha-lemma_sgns.zip) (1830s-2000s) (COHA)
  - [ECCO](http://ryanheuser.org/data/word2vec.ECCO.skipgram_n=10.model.txt.gz). Eighteenth Century Collections Online (ECCO), “Literature and Language,” 1700-99, with 1.9 billion words and trained using word2vec with skip-gram size of 10 words
  - [ECCO20](https://archive.org/details/word-vectors-18c-word2vec-models-across-20-year-periods). ECCO split in twenty-year periods of 18C, with 150 million words each and trained using word2vec with skip-gram size of 10 words
  - [ECCO-TCP](http://ryanheuser.org/data/word2vec.ECCO-TCP.txt.zip). ECCO with 80 million words trained using skip-gram size of 5 words. Also available for [size of 10 words](http://ryanheuser.org/data/word2vec.ECCO-TCP.skipgram_n=10.txt.zip).
- Multi-lingual:
  - [French](http://snap.stanford.edu/historical_embeddings/fre-all_sgns.zip) (1800s-1990s by decade)
  - [German](http://snap.stanford.edu/historical_embeddings/ger-all_sgns.zip) (1800s-1990s by decade)
  - [Simplified Chinese](Simplified Chinese (1950-1990s) (1950-1990s by decade)

## Bias in pre-trained historical word embeddings

Word embeddings allow for analogy checking. For example, man is to king as woman is to queen, expressed as man:king :: woman:queen, has its reflection on the vector representions of the words man, king, woman, queen in such a way that  king→−man→+woman→≈queen→king→−man→+woman→≈queen→ . However, this can also highlight some biases in the specific corpora the model has been trained on. Using as a base the pair she-he, find the most similar term for female from the term in the next list: doctor, captain, gallant, sheriff, engineer, scientist, author, surgeon, honorable, philosopher, warrior, architect, magician, liar, and coward. 
When possible, compute the similarity between the expected term for female and the one for male. Use the Google News (2015), English Fiction (1900, 1950) and Genre-Balanced American English (1900, 1950) embeddings. For example, using the English Fiction 1850 embeddings, he:gallant :: she:x solves to x=gentle, and the similarity between gallant and gentle is ~0.418. Can you spot the problem? 
Hint: Use Gensim's most_similar_cosmul()/most_similar() and similarity() functions

Really cherry-picking the "interesting" results; scroll right past the total nonsense and latch onto anything that can be vaguely thinks

By comparing how different the he:X :: she:X results are, we can quantify the gendered bias within the corpus, to skeptically evaluate our corpora

Very hard to remove gendered bias without removing the other relationships that interest us

Not just corpora that are biased; because the algorithm depends on the corpus, it will become biased too


## Extending Vector Algorithms: Text Classification

Averaging vectors
We've seen that vectors for out of vocabulary words are obtained by splitting the word into its n-grams, getting the embedding for the n-grams, and then averaging the composition to produce the final word vector for the OOV word.

What is best in the word2vec approach is that operations on the vectors approximately keep the characteristics of the words, so that joining (averaging) vectors from the words of a sentence produce a vector that is likely to represent the general topic of the sentence.

Therefore, the same technique used for OOV words in fastText can also be used to produce embeddings for sentences, paragraphs and even entire documents, making it possible for text classification purposes.

> The goal of text classification is to assign documents (such as emails, posts, text messages, product reviews, etc...) to one or multiple categories. Such categories can be review scores, spam v.s. non-spam, or the language in which the document was typed. Nowadays, the dominant approach to build such classifiers is machine learning, that is learning classification rules from examples. In order to build such classifiers, we need labeled data, which consists of documents and their corresponding categories (or tags, or labels).
-- [fastText documentation](https://fasttext.cc/docs/en/supervised-tutorial.html#what-is-text-classification)

Let's see how this way of seeing sentences and documents might actually work. Consider the next dummy sentiment texts with 1 positive sentence and 1 negative sentence.

Now let's get the embeddings for every single word then average them per sentence.

And now, let's get the average vectors por positive and negative sentences.

We can now run the same process for a couple of test sentences and see if their sentence vectors are similar to the positive or the negative one.

Although this approach seems naive, it's still part of the way fastText does its text classification. Moreover, it uses a shallow neural network and ideas similar to CBOW but for word n-grams. The result, which rivals state-of-the-art text classification techniques based on deep learning, runs several orders of magtinude faster.

(His example sentiment analysis works because he made a toy corpus; doesn't do well with sarcasm)

### Doc2Vec

In Gensim, this functionality is under `gensim.models.Doc2Vec`, and it uses a slightly different approach based on Word2Vec, the *Paragraph Vector*, where the model learns to correlate labels and words, rather than words with other words.

> The idea is straightforward: we act as if a paragraph (or document) is just another vector like a word vector, but we will call it a paragraph vector. We determine the embedding of the paragraph in vector space in the same way as words. Our paragraph vector model considers local word order like bag of n-grams, but gives us a denser representation in vector space compared to a sparse, high-dimensional representation. -- [RaRe Technologies](http://nbviewer.jupyter.org/github/RaRe-Technologies/gensim/blob/develop/docs/notebooks/doc2vec-IMDB.ipynb#Paragraph-Vector)

The first step is coming up with a vector that represents the *meaning* of a document, which can then be used as input to a supervised machine learning algorithm to associate documents with labels. There are 2 flavors that are roughly the equivalents of CBOW and Skip-gram. In the **Paragraph Vector Distributed Memory (PV-DM)** model, analogous to CBOW Word2vec, the paragraph vectors are obtained by training a neural network on the fake task of inferring a center word based on context words and a context paragraph. A paragraph is a context for all words in the paragraph, and a word in a paragraph can have that paragraph as a context. In the **Paragraph Vector Distributed Bag of Words (PV-DBOW)** model, analogous to Skip-gram Word2vec, the paragraph vectors are obtained by training a neural network on the fake task of predicting a probability distribution of words in a paragraph given a randomly-sampled word from the paragraph.

Doc2Vec, which considers blocks of texts and units, has built-in support for the equivalent for CBOW as *distributed memory* (`dm`), and *distributed bag of words* (`dbow`) for Skip-gram. Since the distributed memory model performed noticeably better in the paper, that algorithm is the default when running Doc2Vec. You can still force the `dbow` model if you wish, by using the `dm=0` flag in constructor.

### Authorship attribution 

Let's now see an example where we aim to build a classifier for Jane Austen and G.K. Chesterton's works, where each work is assigned a label or tag with its author. Let's also suppose we don't know who the author for Austen's Emma was but we know for sure that is either Austen or Chesterton. One way to approach this is by making building a classifier to predict a label or tag for the unseen anonymous work so we can see who the classifier thinks the work belongs to. This is, with some licenses, a very basic instance of authorship attribution.

We start by obtaining the total number of words and sentences for all their works in the NLTK's Gutenberg corpus and consider that to be all the works that they ever wrote.

```
works = ['austen-emma.txt', 'austen-persuasion.txt', 'austen-sense.txt',
         'chesterton-ball.txt', 'chesterton-brown.txt', 'chesterton-thursday.txt']
for work in works:
    print("{:25} {:8} words {:5} sentences".format(
        work,
        len(nltk.corpus.gutenberg.words(work)),
        len(nltk.corpus.gutenberg.sents(work)))
    )
```

By removing Emma from our list of works, we roughly have the same amount of words per author, which should alleviate the class imbalance issue.

Gensim provides two classes to encode sentences or entire documents: `LabeledSentence()` and `TaggetDocument()`, respectively. While their operation is very similar, the former is intended for short texts and sentences, while the latter performs better for large chunks of text.

Once we have the words from our corpus of works, let's create instances of each of them as `TaggedDocument`s by passing the list of words and the label or tag. We will use the label `anonymous` for Austen's *Emma*. Similarly, we could have built `documents` to have a list of sentences instead and then predict the proportion of sentences in Austen's *Emma* properly assigned to her.

```
from gensim.models.doc2vec import TaggedDocument
    
documents = [
    TaggedDocument(
        words=nltk.corpus.gutenberg.words('austen-persuasion.txt'),
        tags=['austen']),
    TaggedDocument(
        words=nltk.corpus.gutenberg.words('austen-sense.txt'),
        tags=['austen']),
    TaggedDocument(
        words=nltk.corpus.gutenberg.words('chesterton-ball.txt'),
        tags=['chesterton']),
    TaggedDocument(
        words=nltk.corpus.gutenberg.words('chesterton-brown.txt'),
        tags=['chesterton']),
    TaggedDocument(
        words=nltk.corpus.gutenberg.words('chesterton-thursday.txt'),
        tags=['chesterton']),
    TaggedDocument(
        words=nltk.corpus.gutenberg.words('austen-emma.txt'),
        tags=['anonymous']),
]
```

Now, it's time to initialize a `Doc2Vec()` model with some learning rate `alpha`, build the vocabulary from our list of works, and start training over a number of epochs, 10 in this case. The values for `total_examples` and `epochs` are the default ones, although for some reason `Dov2Vec()` forces you to pass them in explicitly: `total_examples=model.corpus_count` and `epochs=model.epochs`.

```
from gensim.models import Doc2Vec

model = Doc2Vec(min_cout=0)
model.build_vocab(documents)
for epoch in tqdm(range(10), desc='Epochs'):
    model.train(documents, total_examples=model.corpus_count, epochs=model.epochs)
```

Need to run in many epochs -- 10 would be fine for this small practice corpus, but a larger one at least 50.

Once the model has been fit to our corpus, we have available the usual functions from word2vec but for documents, `docs2vec`.

Let's see, from our list of tags that represent the authors of the works, which one 'anonymous' is more similar to:

```
model.docvecs.most_similar_to_given('anonymous', ['austen', 'chesterton'])
```

Finally, let's compute similarity and distance from Austen's Emma (anonymous) to the vectors that represent Jane Austen and Chesterton.

```
for author in ('austen', 'chesterton'):
    print(author)
    print("\tSimilarity", model.docvecs.similarity('anonymous', author))
    print("\tDistance", model.docvecs.distance('anonymous', author))
```

#### Doing it again on the sentence level:

<div align="right"><small class="text-muted">*Double click here to see the full code solution*</small></div>

- 1. Build the list of sentences, prefixing each one with __label__author
texts = []
```
for work in works:
    for sent in nltk.corpus.gutenberg.sents(work):
        if 'emma' not in work:  # Our anonymous work!
            author = work.split('-')[0]
            sentence = ' '.join(sent)
            texts.append(f"__label__{author} {sentence}")
```

- 2. Randomly split the list in training and testing
```
training_size = int(np.floor(len(texts) * 0.75))
np.random.shuffle(texts)
training, testing = texts[:training_size], texts[training_size:]
```

- 3. Get the texts from the training and testing lists
```
training_text = '\n'.join(training).strip()
testing_text = '\n'.join(testing).strip()
```

- 4. Create the temporary files so fastText can read them 
```
with open('author_train.txt', 'w') as f:
    f.write(training_text)
with open('author_test.txt', 'w') as f:
    f.write(testing_text)
```

- 5. Build a classifier and test it on the testing sentences
```
classifier = fasttext.supervised('author_train.txt', 'author_model')
result = classifier.test('author_test.txt')
print('Precision:', result.precision)
print('Recall:', result.recall)
print('Number of sentences:', result.nexamples)
```

- 6. For each sentence in Austen's Emma, predict its author
```
emma_sentences = [' '.join(sent)
                  for sent in nltk.corpus.gutenberg.sents('austen-emma.txt')]
predictions = classifier.predict(emma_sentences)
```

- 7. Print the percentage of sentences from Austen' Emma associated to each author
```
authors, counts = np.unique(predictions, return_counts=True)
counts = counts / sum(counts)
print()
print("Predicting Austen's Emma's sentences")
for author, percentage in zip(*[authors, counts]):
    print(f"{author.capitalize()} accounts for {100*percentage:.2f}% of sentences.") 
```

The binary classifier will **always** give an answer of one of the two options that we gave it.

# 4. Role of Bias in Word Embeddings
[Didn't have time for this but would be cool to look at]
In this unit, we will explore an application and caveat of using word embeddings -- cultural bias. Presenting methods and results from recent articles, we will show how word embeddings can carry the historical biases of the training corpora and lead an activity that shows these human-biases on vectors. We'll also address how such bias can be mitigated.



0:00 - 0:10 Algorithmic bias vs human bias
0:10 - 0:40 Identifying bias in corpora (occupations, gender, ...)
0:40 - 0:50 Towards unbiased embeddings; Examine “debiased” embeddings
0:50 - 0:60 Concluding remarks and debate