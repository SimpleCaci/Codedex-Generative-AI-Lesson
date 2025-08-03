import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')


sample_text = "Sample Text: Beep Boop"
tokens = word_tokenize(sample_text)
print("Tokens:", tokens)