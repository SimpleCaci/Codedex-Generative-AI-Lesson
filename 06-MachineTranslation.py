from translate import Translator

translator = Translator(to_lang='es') 

text = 'Hello, How are you?'

translation = translator.translate(text)

print('Translated Text:', translation)