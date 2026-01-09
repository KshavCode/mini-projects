from tkinter import * 
from tkinter.messagebox import *
from PIL import Image, ImageTk as imtk
import qrcode
import os

def new() :
    linkk = linkvar.get()
    if linkk == "" or linkk.isspace() == True  or  " " in linkk :
        showerror("ERROR!", "Looks like you didn't enter a link :(") 
    else : 
        img = qrcode.make(linkk)
        img.show(img)


root = Tk() 
root.geometry("400x150")
root.title("QR Code Generator")
root.resizable(False, False)

linkvar = StringVar()
linklab = Label(root, text="Link : ", font="helvetica 13 bold")
linkentry = Entry(root, textvariable=linkvar, width=30, font="comicsansms 10 ")
linkconf = Button(root, text="Generate Code", highlightthickness=4, command=new)

linklab.place(relx=0.2, rely=0.08)
linkentry.place(relx=0.35, rely = 0.09)
linkconf.place(relx=0.4, rely=0.4)


root.eval('tk::PlaceWindow . center')

root.mainloop()