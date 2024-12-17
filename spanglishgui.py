from tkinter import * 
from english import spanishToEnglish
from spanish import englishToSpanish

root = Tk()
root.title("Spanglish: Language Translator")
root.geometry('693x675')
root.resizable(0,0)
label = None
def spanishActivate():
    clickSpanish.config(bg="red")
    clickEnglish.config(bg="white")
    translateLabel = Label(root, text = "What would you like to translate?", font=("Helvetica", 15, "bold"), fg = "red", justify = "center", padx = 10, pady = 10)
    translateLabel.grid(row = 3, column = 0, columnspan = 2, pady=20, sticky="nsew")
    global tEntry
    tEntry = Entry(root, width = 25, borderwidth = 5, justify = "center")
    tEntry.grid(row=5, column=0, columnspan = 2, pady=20, sticky="nsew")
    buttonClick = Button(root, text = "Click to confirm", command= spanishTranslate, justify = "center", padx = 10, pady = 10, font=("Helvetica", 12, "bold"))
    buttonClick.grid(row = 7, column=0, columnspan = 2, pady=10, sticky="nsew")

def englishActivate():
    clickEnglish.config(bg="red")
    clickSpanish.config(bg = "white")
    translateLabel = Label(root, text = "What would you like to translate?", font=("Helvetica", 15, "bold"), fg = "red", justify = "center", padx = 10, pady = 10)
    translateLabel.grid(row = 3, column = 0, columnspan = 2, pady=20, sticky="nsew")
    global tEntry
    tEntry = Entry(root, width = 25, borderwidth = 5, justify = "center" )
    tEntry.grid(row = 5, column= 0, columnspan = 2, pady=20, sticky="nsew")
    buttonClick = Button(root, text = "Click to confirm", command= englishTranslate, justify = "center", padx = 10, pady = 10, font=("Helvetica", 12, "bold"))
    buttonClick.grid(row = 7, column = 0, columnspan = 2, pady=10, sticky="nsew")

def spanishTranslate():
    global label
    
    if label: 
        label.destroy()
    label = Label(root, text = spanishToEnglish(tEntry.get()), font=("Helvetica", 12, "bold"), borderwidth = 10, bg = "white", wraplength=325, justify = "center", padx = 20, pady = 20)
    label.grid(row = 15, column=0, columnspan = 3, pady=20, sticky="nsew")

    
def englishTranslate():
    global label 
    
    if label: 
        label.destroy()
    label = Label(root, text = englishToSpanish(tEntry.get()), font=("Helvetica", 12, "bold"), borderwidth = 10, bg = "white", wraplength=325, justify = "center", padx = 20, pady = 20)
    label.grid(row = 15, column=0, columnspan = 3, pady=20, sticky="nsew")
    

def clickEnglish():
    englishActivate()

def clickSpanish():
    spanishActivate()


mylabel = Label(root, text= "Welcome to Spanglish! Which language would you like to translate? (English or Spanish)", bg="Orange", padx = 45, pady = 50, font = 5)
mylabel.grid(row = 0, column = 0, columnspan=3)



clickEnglish = Button(root, text = "English", padx = 125, pady = 50, borderwidth = 5, font=("Helvetica", 12, "bold"), command = clickEnglish,)
clickEnglish.grid(row=2, column=0, pady = 5)

clickSpanish = Button(root, text = "Spanish", padx = 125, pady = 50, borderwidth = 5, font=("Helvetica", 12, "bold") ,command=clickSpanish,)
clickSpanish.grid(row=2, column=1, pady = 5)

root.mainloop()