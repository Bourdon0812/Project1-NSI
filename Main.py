from tkinter import *


def genWindow():
    window = Tk()
    window.title("Mot de passe")
    window.iconbitmap("resources\logo.ico")
    window.geometry("720x480")
    window.minsize(720, 480)
    window.maxsize(720, 480)
    window.mainloop()


genWindow()