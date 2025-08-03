#Naive Bayes Classifier (A type of auto sorting tool in machine learning using Bayes' Theorem)
#WAIT I LEARNED THIS IN MATH CLASS
#P(A|B) = [P(B|A) x P(A) ] / P(B)
# A few things we will use:
'''
CountVectorizer - text -> word frequency
MultinomialNB - THE NAIVE BAYES CLASSIFER MODEL?
    - each catagory is given a score based on about
            P(class) x P(word1|class) x P(word2|class)
            P(class) x [P(class|word1)xP(word1)/P(class)] x [P(class|word2)xP(word2)/P(class)]
train_test_split - splits one set of data for training and the other one for testing
accuracy_score - how good the prediction is  (1.0 = best)
'''

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

texts = [
  'I love programming.', 'Python is amazing.',
  'I enjoy machine learning.', 'The weather is nice today.', 'I like algo.',
  'Machine learning is fascinating.', 'Natural Language Processing is a part of AI.'
]

labels = [
  'tech', 'tech', 'tech', 'non-tech', 'tech', 'tech', 'tech'
] #corresponding to the texts

vectorizer = CountVectorizer()
x = vectorizer.fit_transform(texts)


x_train, x_test, y_train, y_test = train_test_split(x, labels, test_size=0.2, random_state=42)


model = MultinomialNB()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)