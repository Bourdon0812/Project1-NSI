from tkinter import *

window = Tk()

def onDisconect():
    window.destroy()


def genWindow(win: Tk):
    win.title("Mot de passe")
    win.iconbitmap("resources\logo.ico")
    win.geometry("720x480")
    win.minsize(720, 480)
    win.maxsize(720, 480)
    win.config(background="#535353")


genWindow(window)

title = Label(window, text="Mise à jour de votre mot de passe", font=("Arial", 30), fg="white", bg="red", relief=SUNKEN)
title.pack(fill=X)

baseFrame = Frame(window, bg="#535353")

img = PhotoImage(file="resources\logo.png").zoom(2).subsample(20)
canvas = Canvas(baseFrame, width=75, height=75, bg="#535353", bd=0, highlightthickness=0)
canvas.create_image(
    75/2,
    75/2,
    image=img
)
canvas.grid(row=0, column=0, sticky=W)

disconectButton = Button(baseFrame, text="Déconexion", font=("arial", 10), bg="#535353", command=onDisconect)
disconectButton.grid(row=0, column=1, sticky=E, padx=550)

baseFrame.pack(fill=X)

window.mainloop()
