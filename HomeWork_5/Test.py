from tkinter import Tk, BOTH
from tkinter.ttk import Frame, Button, Style


class Visual(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")
        self.parent = parent
        self.parent.title("Игра пиратская нажива")
        self.pack(fill=BOTH, expand=1)
        self.centerWindow()
 
    def centerWindow(self):
        w = 290
        h = 150
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        x = (sw - w) / 2
        y = (sh - h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))
    
    def initUI(self):
        self.style = Style()
        self.style.theme_use("default")
        quitButton = Button(self, text="Выход", command=self.quit)
        quitButton.place()


def main():
    root = Tk()
    root.geometry("600x480+300+300")
    app = Visual(root)
    root.mainloop()  
 
if __name__ == '__main__':
    main()