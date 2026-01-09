from tkinter import * 
from tkinter import messagebox
import clipboard

import requests

root = Tk()
root.geometry("300x200")
root.title("URL Shortner")



def change() : 
    link = linkvar.get()
    url = "https://api.apilayer.com/short_url/hash"

    payload = f"{link}".encode("utf-8")
    headers= {"apikey": "oSuyI00nLsek8z5xMbX6DOp7PHrFgrmM"}
    response = requests.request("POST", url, headers=headers, data = payload)
    try:
        result = response.json()["short_url"]
        messagebox.showinfo("SUCCESS!", "The shortened link has been copied to your clipboard!")
        clipboard.copy(result)
    except : 
        messagebox.showerror("FAILED!", "Seems like you gave an invalid link :(")
    
    
    
def unloading() : 
    linkvar.set("")


linkvar = StringVar()

linklab = Label(root, text="Enter the link : ", font="monospace 12")

linkent = Entry(root, textvariable=linkvar)

shot = Button(root, text="Shorten", command=change, width=15, font="13", relief=GROOVE, background="lightblue")
unload = Button(root, text="Clear", command=unloading, width=15, font="13", relief=GROOVE, background="lightpink")

linklab.place(relx=0.07, rely=0.205)
linkent.place(relx=0.45, rely=0.22)
shot.place(relx=0.25, rely=0.4)
unload.place(relx=0.25, rely=0.6)
root.mainloop()  