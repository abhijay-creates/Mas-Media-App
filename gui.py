import tkinter as tk
#importing tkinter
from tkinter import ttk
#importing widgets thingy




def on_click():
    label.config(text="Clicked")
#the func to express clicking


#I'm gonna make a function for the objective of opening another window, for example twitter, 
#and run an image on that ,using a buttoon
def go_to_twit():
    root1 = tk.Tk()
    root1.geometry("500x500")
    root1.mainloop()
    pass




root = tk.Tk()
#root is the base for the app- the bg- the foundation

root.geometry("360x800")
root.title("Title")



label = tk.Label(root, text = "Label 1", font =("Times New Roman",14))
button = tk.Button(root, text = "Button 1", command=on_click)

twitter_button = tk.Button(root,text = "Twitter",activebackground="red",command=go_to_twit)
twitter_button.pack()



label.pack(pady=(20,100))
#place label
button.pack(pady=(50,150))
#place button below label

root.mainloop()