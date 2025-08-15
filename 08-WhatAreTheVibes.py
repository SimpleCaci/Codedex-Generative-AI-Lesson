#building a tool to see if you should watch a movie based on text and reviews

from sklearn.feature_extraction.text import CountVectorizer #text -> numbers
from sklearn.naive_bayes import MultinomialNB #word counts frequency analyzation 
from sklearn.model_selection import train_test_split #training set and test set
from sklearn.metrics import accuracy_score #prediction measurement


#TRAINING DATA
'''
reviews = ['This movie was fantastic! A must-watch.',
           'I didn\'t enjoy this movie at all and dull and dull.',
           'Amazing storyline and great acting!',
           'The plot was dull and predictable and dull and dull.',
           'Loved the cinematography! Highly recommended.'] #in a normal program, this is not enough data to test or train a model

labels = ['positive', 'negative', 'positive', 'negative', 'positive']
'''

#new data
reviews = [
    "This movie was fantastic! A must-watch.",
    "I didn't enjoy this movie at all and dull and dull.",
    "Amazing storyline and great acting!",
    "The plot was dull and predictable and dull and dull.",
    "Loved the cinematography! Highly recommended.",
    "Brilliant performance and heartfelt story.",
    "Terrible script, flat characters, and poor acting.",
    "Visually stunning with an unforgettable soundtrack.",
    "Boring from start to finish, I almost fell asleep.",
    "An inspiring and uplifting film worth seeing twice."
]

labels = [
    "positive",  # 1
    "negative",  # 2
    "positive",  # 3
    "negative",  # 4
    "positive",  # 5
    "positive",  # 6
    "negative",  # 7
    "positive",  # 8
    "negative",  # 9
    "positive"   # 10
]



vectorizer = CountVectorizer()
x = vectorizer.fit_transform(reviews)

x_train, x_test, y_train, y_test = train_test_split(x, labels, test_size=0.2, random_state=42)

model = MultinomialNB()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)

print('Accuracy:', accuracy)

if accuracy > 0.8:
  print('Good vibes. Book the ticket!')
else:
  print('Needs more work!')

'''

'''