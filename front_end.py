#used https://www.youtube.com/watch?v=ddoPYppcppc to create the window with tinker and created the front end
#importing the libraries using tkinter

from tkinter import *

#function for onclick 

def onclick():
    import text_reading #imports the functions of the text_reading that takes in the voice

#creating the window 
window = Tk()

#creating labels
l1 = Label(window, text = "SIMPL Project Name: ")
l1.grid(row = 0, column = 0)

l2 = Label(window, text = "Project Name:")
l1.grid(row = 0, column = 1)

#entriies text input
label_text = StringVar()
el = Entry(window,textvariable=label_text)
el.grid(row=0,column = 2)

#creating a list box

list1 = Listbox(window, height = 20, width = 70)
list1.grid(row = 2, column = 1, rowspan = 6 ,columnspan = 2)

#creating a scroll with list box

sbl = Scrollbar(window)
sbl.grid(row=2,column=3,rowspan = 1)

list1.configure(yscrollcommand = sbl.set)
sbl.configure(command=list1.yview)

#butttons
b1 = Button(window, text = "Begin", width = 12, command = onclick)
b1.grid(row = 0, column = 3)




window.mainloop()