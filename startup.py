from tkinter import *
import os

#please read the readme before doing anything

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack(fill=BOTH, expand=1)

        self.var1=IntVar()
        self.var2=IntVar()
        self.var3=IntVar()
        self.var4=IntVar()

        Placeholder1=Checkbutton(self, text="Placeholder", variable=self.var1, onvalue=1, offvalue=0)
        Placeholder1.place(x=10,y=10)
        Placeholder2=Checkbutton(self, text="Placeholder", variable=self.var2, onvalue=1, offvalue=0)
        Placeholder2.place(x=10,y=35)
        Placeholder3=Checkbutton(self, text="Placeholder", variable=self.var3, onvalue=1, offvalue=0)
        Placeholder3.place(x=10,y=60)
        Placeholder4=Checkbutton(self, text="Placeholder", variable=self.var4, onvalue=1, offvalue=0)
        Placeholder4.place(x=10,y=85)
        
        startButton=Button(self, text="start", command=self.startSelected)
        startButton.place(x=155,y=15)

        exitButton=Button(self, text="cancel", command=self.clickExitButton)
        exitButton.place(x=150, y=80)

    def startSelected(self):
        if(self.var1.get() == 1):
            os.startfile('"placeholder"')
        elif(self.var1.get() == 0):
            pass
        
        if(self.var2.get() == 1):
            os.startfile('"placeholder"')
        elif(self.var2.get() == 0):
            pass
        
        if(self.var3.get() == 1):
            os.startfile('"placeholder"')
        elif(self.var3.get() == 0):
            pass
        
        if(self.var4.get() == 1):
            os.startfile('"placeholder"')
        elif(self.var4.get() == 0):
            pass

            
    def clickExitButton(self):
        sys.exit()

root = Tk() 
root.wm_title("startup") 
app = Window(root)
root.geometry("220x120")
root.resizable(width=False, height=False)
root.mainloop()
