from tkinter import *

class Window(Frame) :

    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.master = master
        print("master=none means this is the main window, and has no parent")


root = Tk()
app = Window(root)
root.mainloop()
app.widgetName="something"
        
