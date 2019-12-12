from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from separateur_createur_video import tracking

class Root(Tk):

    def __init__(self):
        super(Root, self).__init__()
        self.title("Tracking couleur")
        self.minsize(640,240)
        #self.wm_iconbitmap('icon.ico')


        self.labelFrame = ttk.LabelFrame(self, text = "Open A File")
        self.labelFrame.grid(column = 0,row = 1, padx = 20, pady = 20)


        self.button()
        self.mybutton()
        self.buttonDest()


    def button(self):
        self.button = ttk.Button(self.labelFrame, text = "choisir une vidéo", command = self.fileDialog)
        self.button.grid(column = 1, row = 1)

    def buttonDest(self):
        self.button = ttk.Button(self.labelFrame, text = "choisir dossier destination", command = self.fileDialogDest)
        self.button.grid(column = 2, row = 1)


    def mybutton(self):
        self.button = ttk.Button(self.labelFrame, text = "lancer le tracking",command = lambda: tracking(str(self.fileDialog),str(self.fileDialogDest)))
        self.button.grid(column = 3, row = 1)

    def fileDialog(self):
        
        self.filename = filedialog.askopenfilename(initialdir = "C:\\", title = "Select A File", filetype= (("*.mp4","*.avi"), ("All files", "*.*")))

        self.label = ttk.Label(self.labelFrame, text = "")
        self.label.grid(column = 1,row = 2)
        self.label.configure(text = self.filename)

        return self.filename

    def fileDialogDest(self):
        
        self.filename = filedialog.askdirectory(initialdir = "C:\\", title = "Select A Folder")
        
        self.label = ttk.Label(self.labelFrame, text = "")
        self.label.grid(column = 1,row = 3)
        self.label.configure(text = self.filename)

        return self.filename



if __name__== '__main__':
    root = Root()
    root.mainloop()
 
