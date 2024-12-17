from googletrans import Translator

translator = Translator()

done = translator.translate("Hello", dest="en")

print(done.text)