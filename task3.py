import os
from tkinter import *
path='/Users/manmohan/desktop/'
files = os.listdir(path)
print(files)


root = Tk()
root.geometry( "200x200" )
clicked1 = StringVar()
clicked1.set( "select the file" )
drop1 = OptionMenu( root , clicked1 , *files )
drop1.pack()


def show():
    filename = clicked1.get() 
    try:
        s="python " + filename
        print(s)
        os.system(s)  
    except:
        print("file is not a python file")    


button = Button( root , text = "click Me" , command = show ).pack()
root.mainloop()
  