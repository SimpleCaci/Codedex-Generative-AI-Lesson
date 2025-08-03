#N-gram
#unigram
#bigram
#trigramn
#ngram
#basically using frequency of consecutive characters or words to predict 


import nltk
from nltk.tokenize import word_tokenize
from nltk.util import ngrams

sample_text = "I am learning NLP"
tokens = word_tokenize(sample_text)
unigrams = list(ngrams(tokens, 1)) #unigram
print(unigrams)
bigrams = list(ngrams(tokens, 2)) # Bigram
print(bigrams)
trigrams = list(ngrams(tokens, 3)) #trigram
print(trigrams)