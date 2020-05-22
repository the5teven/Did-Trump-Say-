#!/usr/bin/env python3
# -*-coding: utf8-*-

import tkinter as tk
import pickle
from  PIL import  ImageTk,Image
import time
class Who:
    TRUMP = 'TRUMP'
    NOT_TRUMP = 'NOT_TRUMP'

# Model Files
file_cfl = 'Models/trump_classifier.pkl'
file_vec = 'Models/vectorizer.pkl'

#open files
with open (file_cfl,'rb') as f:
    clf = pickle.load(f)
with open (file_vec,'rb') as f:
    vectorizer = pickle.load(f)


class GUI:
    def __init__(self, master,bg_image):
        self.master = master

        self.canvas = tk.Canvas(master, width=550,height=250,highlightthickness=0)
        self.canvas.create_image(0,0,anchor=tk.NW,image=bg_image)
        self.canvas.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.label = tk.Label(self.master,text='DID TRUMP SAY IT?',background='#2b3362',foreground='white',font=("futura", 20))
        self.label.place(relx=0.5, rely=0.245, anchor=tk.CENTER)

        self.outline = tk.Canvas(self.master,width=360,height=73,bg='#d92725',highlightbackground='#d92725')
        self.outline.place(relx=0.5, rely=0.45, anchor=tk.CENTER)
        self.text = tk.Text(self.master,width=50,height=4.5)
        self.text.place(relx=0.5, rely=0.45, anchor=tk.CENTER)
        self.button = tk.Button(self.master, height=1, width=40, text="Enter",highlightthickness=0 ,bg= '#d92725' , command=lambda: self.retrieve_input())
        self.button.place(relx=0.5, rely=0.67, anchor=tk.CENTER)
    def retrieve_input(self):
        inputValue = self.text.get("1.0", "end-1c")
        didhe= did_he_say(inputValue,clf,vectorizer)
        if inputValue == '':
            self.label.config(text='DID TRUMP SAY IT?',foreground='white')
            self.outline.config(bg='#d92725',highlightbackground='#d92725')
        elif didhe == Who.TRUMP:
            self.label.config(text='SOUNDS LIKE SOMETHING HE WOULD SAY!',foreground='Green')
            self.outline.config(bg='green',highlightbackground='green')
        elif didhe == Who.NOT_TRUMP:
            self.label.config(text='DOES NOT SEEM LIKE SOMETHING HE WOULD SAY!', foreground='#d92725')
            self.outline.config(bg='#d92725', highlightbackground='#d92725')


def did_he_say(text,clf,vectorizer):
    v_text = vectorizer.transform([text])
    prediction = clf.predict(v_text)
    return(prediction[0])




root = tk.Tk()
root.config(bg='#2b3362')
image = ImageTk.PhotoImage(Image.open('Images/background.png'))
root.minsize(550,250)
root.maxsize(550,250)
gui=GUI(root,image)




root.mainloop()

