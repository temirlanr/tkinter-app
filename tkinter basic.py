from tkinter import *

root = Tk()

#####
# myLabel1 = Label(root, text="Hello World!")
# myLabel2 = Label(root, text="My name is TemirlaN!!!")
# myLabel3 = Label(root, text="       ")

# myLabel1.grid(row=0, column=0)
# myLabel2.grid(row=1, column=5)
# myLabel3.grid(row=2, column=2)
#####

def myClick():
    myLabel = Label(root, text="ClickED!!")
    myLabel.pack()

myButton = Button(root, text="Click", padx=50)
myButton.pack()



root.mainloop()