from googletrans import Translator
translator = Translator()



def spanishToEnglish(name) -> str:
    done = translator.translate(name, dest="en")
    return done.text
