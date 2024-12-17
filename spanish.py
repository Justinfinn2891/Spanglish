from googletrans import Translator 
translator = Translator()

def englishToSpanish(name) -> str:
    done = translator.translate(name, dest="es")
    return done.text
