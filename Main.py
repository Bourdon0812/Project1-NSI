#
#                                   Project 1 NSI
#
#   Systéme de validation de changement de mot de passe en python sous interface graphique à l'aide du module
#   Tkinter
#
#

from tkinter import *
from tkinter.messagebox import *
from utils.Libs import *


# Fonction appelé lorsque le bouton confirmer est cliqué
def submitPassword():
    # dans le cas ou le mot de passe est pas valide on envoi une erreur et explique la raison
    if not isValid(mdpInput.get()):
        showerror("Mot De Passe", "Votre mot de passe n'est pas valide car" + getNoValidReason(mdpInput.get()))
        return
    # de meme ici, on verifie si le mot de passe confirmer correspond
    if mdpInput.get() != mdpConfirmInput.get():
        showerror("Mot De Passe", "Les 2 mot de passe ne correspondent pas")
        return
    showinfo("Mot De Passe", "Votre mot de passe a été changé avec succés, vous pouvez fermer les pages")


# Fonction appelé lorsque le bouton de deconexion est pressé alors on ferme la fenetre
def onDisconect():
    window.destroy()


# Cette fonction est appelé lorsque une touche du clavier est relaché, elle a pour but d'update les cases
# en rouge ou en verte en fonction des criteres respecté ou non
def keyPressEvent(event):
    setLine4(mdpInput.get())


# Génération de la base de la fenetre : titre, resolution, icone, couleur de fond etc
def genWindow(win: Tk):
    win.title("Mot de passe")
    win.iconbitmap("resources\logo.ico")
    win.geometry("720x480")
    win.minsize(720, 480)
    win.maxsize(720, 480)
    win.config(background="#535353")


# generation de l'image presente en haut a gauche ainsi que de la creation du bouton de déconexion
def setLine1():
    # obligé de la globalisé sinon la variable se detruit apres l'execution de la fonction et donc elle disparait sur l'interface
    global img
    line1: Frame = Frame(baseFrame, bg="#535353")

    imgFrame = Frame(line1, bg="#535353")

    canvas: Canvas = Canvas(imgFrame, width=75, height=75, bg="#535353", bd=0, highlightthickness=0)
    canvas.create_image(
        75 / 2,
        75 / 2,
        image=img
    )
    canvas.pack()

    imgFrame.grid(row=0, column=0, sticky=W)

    disconectButton: Button = Button(line1, text="Déconnexion", font=("arial", 10), fg='#ffffff', bg="red",
                                     command=onDisconect)
    disconectButton.grid(row=0, column=1, sticky=E, padx=550)
    line1.grid(row=0, column=0, sticky=W)


# generation du cadre expliquant les criteres à respecter afin d'avoir un mot de passe valide
def setLine2():
    line2: Frame = Frame(baseFrame, bg="#535353")
    infoFrame: Frame = Frame(line2, bg="#535353", bd=2, relief=SUNKEN)

    infoTitle: Label = Label(infoFrame, text="Politique de sécurité : ", font=("Arial", 17, "bold"), fg="red",bg="#535353")
    infoTitle.grid(row=0, column=0, sticky=W)

    infoRequire: Label = Label(
        infoFrame,
        text="Le mot de passe doit contenir au minimum : \n  ➤ 8 caractères \n  ➤ 1 majuscule \n  ➤ 1 minuscule \n  ➤ 1 chiffre ou 1 caractere spécial",
        font=("Arial", 13),
        fg="#ffffff",
        bg="#535353",
        justify=LEFT
    )
    infoRequire.grid(row=1, column=0, sticky=W)
    infoFrame.grid(row=1, column=1, sticky=W, padx=175)
    line2.grid(row=1, column=0, sticky=W)


# Generation de  l'inputt permettant de saisir le mot de passe
def setLine3():
    global mdpInput
    line3: Frame = Frame(baseFrame, bg="#535353")

    mdpLabbel: Label = Label(line3, text="Saisissez votre mot de passe : ", font=("Arial", 13, "bold"), fg="red",
                             bg="#535353")
    mdpLabbel.grid(row=0, column=0, sticky=W, padx=20)

    mdpInput = Entry(line3, font=("arial", 13), bg="#535353", fg="white")
    mdpInput.grid(row=0, column=1, sticky=W)
    mdpInput.bind("<KeyRelease>", keyPressEvent)

    line3.grid(row=2, column=0, sticky=W, pady=25)


# generation des voyant vert et rouge en fonction des criteres respecté ou non (1 voyant vert par criteres respecté)
def setLine4(mdp: str):
    line4: Frame = Frame(baseFrame, bg="#535353")

    for i in range(getMDPLevelSecurity(mdp)):
        lvlLabbel = Label(line4, text="🟩", font=("Arial", 25), bg="#535353", fg="green")
        lvlLabbel.grid(row=0, column=i, sticky=W)
    for i in range(4 - getMDPLevelSecurity(mdp)):
        lvlLabbel = Label(line4, text="🟩", font=("Arial", 25), bg="#535353", fg="red")
        lvlLabbel.grid(row=0, column=getMDPLevelSecurity(mdp) + i, sticky=W)

    line4.grid(row=3, column=0, sticky=W, padx=300)


# generation du champ de texte permettant de confirmer le mot de passe ainsi que du bouton de soumission
def setLine5():
    global mdpConfirmInput
    line5: Frame = Frame(baseFrame, bg="#535353")

    mdpLabbel: Label = Label(line5, text="Confirmer votre mot de passe :", font=("Arial", 13, "bold"), fg="red",
                             bg="#535353")
    mdpLabbel.grid(row=0, column=0, sticky=W, padx=20)

    mdpConfirmInput = Entry(line5, font=("arial", 13), bg="#535353", fg="white")
    mdpConfirmInput.grid(row=0, column=1, sticky=W)

    buttonConfirm: Button = Button(line5, text="Confirmer", font=("arial", 20), fg='#ffffff', bg="red",
                                   command=submitPassword)
    buttonConfirm.grid(row=0, column=2, sticky=W, padx=90)

    line5.grid(row=4, column=0, sticky=W, pady=25)


window: Tk = Tk()
genWindow(window)
mdpInput: Entry | None = None
mdpConfirmInput: Entry | None = None
title: Label = Label(window, text="Mise à jour de votre mot de passe", font=("Arial", 30), fg="white", bg="red",
                     relief=SUNKEN)
title.pack(fill=X)
baseFrame: Frame = Frame(window, bg="#535353")

img: PhotoImage = PhotoImage(file="resources\logo.png").zoom(2).subsample(20)

setLine1()
setLine2()
setLine3()
setLine4("")
setLine5()

baseFrame.pack(fill=X)
window.mainloop()
