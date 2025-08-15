#there are two parts to spell checking
# 1. dictionary comparison (basically comparing to see if there's a similar word, if not, flag it as a MISTAKE) 
# 2. Suggesting Corrections 

from textblob import TextBlob
text = 'i loeve progammming and machine learnig.'

blob = TextBlob(text)

corrected_text = blob.correct()

print('og text:', text)
print('corrected text:', corrected_text)

#possibly be able to use this when doing text input detection