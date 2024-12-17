from english import spanishToEnglish
from spanish import englishToSpanish

def menuText():
    print("Welcome to the Spanglish translator, which language would you like to translate to?")
    print("1.) Spanish to English")
    print("2.) English to Spanish")

def menu():
    
    menuText()

    key = int(input())

    if key == 1:
        translate = spanishToEnglish(input("What would you like to translate?"))
    if key == 2:
        translate = englishToSpanish(input("What would you like to translate?"))

    print(translate)

menu()