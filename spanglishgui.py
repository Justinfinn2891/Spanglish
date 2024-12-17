from tkinter import * 
from english import spanishToEnglish
from spanish import englishToSpanish

root = Tk()
root.title("Spanglish: Language Translator")


def spanishActivate():
    translateLabel = Label(root, text = "What would you like to translate?")
    translateLabel.pack()
    global tEntry
    tEntry = Entry(root, width = 50, borderwidth = 5)
    tEntry.pack()
    buttonClick = Button(root, text = "Click to confirm", command= spanishTranslate)
    buttonClick.pack()

def englishActivate():
    translateLabel = Label(root, text = "What would you like to translate?")
    translateLabel.pack()
    global tEntry
    tEntry = Entry(root, width = 50, borderwidth = 5)
    tEntry.pack()
    buttonClick = Button(root, text = "Click to confirm", command= englishTranslate)
    buttonClick.pack()

def spanishTranslate():
    label = Label(root, text = spanishToEnglish(tEntry.get()))
    label.pack()
    
def englishTranslate():
    label = Label(root, text = englishToSpanish(tEntry.get()))
    label.pack()
    
def click():
    active = 0
    if spanEntry.get() == "Spanish":
        spanishActivate()
        active = 1
    if spanEntry.get() == "English":
        englishActivate()
        active = 1
    if active == 0:
        label = Label(root, text = "ERROR!")
        label.pack()
    

mylabel = Label(root, text= "Welcome to Spanglish! Which language would you like to translate? (English or Spanish)", bg="Orange")
mylabel.pack()

spanEntry = Entry(root, width = 50, borderwidth = 5)
spanEntry.pack()

clickConfirm = Button(root, text = "Click to confirm", command=click)
clickConfirm.pack()

#clickButton = Button(root, text = "Click to translate")

root.mainloop()