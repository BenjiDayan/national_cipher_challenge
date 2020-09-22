#Cipher solvers
from tkinter import *
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', \
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def shift(text, shift):
    """Shifts all characters in text by shift amount.
    e.g. text = 'abc', shift = 1, output = 'bcd'
    """
    decrypted_text = ''
    for char in text:
        decrypted_text += alphabet[(alphabet.index(char)+shift)%26]

    return(decrypted_text)
    
def clean(text):
    """Removes punctuation, and renders all to lower case."""
    cleaned_text = ''
    for char in text:
        if char.lower() in alphabet:
            cleaned_text += char
    return(cleaned_text)


class monoSolver():
    def __init__(self, text):
        self.text = clean(text)
        self.root = Tk()
        self.frame = Frame(self.root)

        self.textDisplay = Label(self.frame, text=self.text, width=10, wraplength=100)
        self.textDisplay.grid(row=0, column=0, sticky="nswe")

        self.substitutions = []
        self.substitutionsFrame = Frame(self.frame)
        self.substitutionsDisplay = []
        for num in range(26):
            texticles = alphabet[num] + ' ='
            self.substitutionsDisplay.append([Label(self.substitutionsFrame, text=texticles),\
                                              Entry(self.substitutionsFrame)])
            self.substitutionsDisplay[-1][0].grid(row=num, column=0)
            self.substitutionsDisplay[-1][1].grid(row=num, column=1)
        self.substitutionsFrame.grid(row=0, column=1, sticky=NW)
        self.frame.pack()
        self.root.mainloop()
        
        
