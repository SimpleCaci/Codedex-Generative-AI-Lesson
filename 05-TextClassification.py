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