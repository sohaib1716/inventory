from googletrans import Translator

translator = Translator()
translation = translator.translate("hello", dest='hi')

print(translation.text)