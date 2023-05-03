from tkinter import *
import cadastro

janela = Tk()
janela.geometry("1024x768")
janela.minsize(1024, 768)
janela.maxsize(1920,1080)
janela.title("Tela de reservas")

rotuloDoTitulo = Label(janela, bg="dark blue", width=180, height=6)
rotuloDoTitulo.pack()

titulo1 = Label(janela, text="Wyden Hotel", font=("Wyden Hotel", 20), bg="dark blue", fg="white")
titulo1.pack()
titulo1.place(x=640, y=25)

titulo2 = Label(janela, text="Quartos:", font=("Quartos", 18))  
titulo2.pack()

global Quarto
Quarto = 1
def BtnBox(quarto,x,y):
  btnBox = Button(janela, text=quarto, font=(quarto, 25), bg="green", fg="white", width=5, height=2)
  btnBox.pack()
  btnBox.place(x=x,y=y)
cadastro.cadastro()

BtnBox("5A",475,150)
BtnBox("5B",600,150)
BtnBox("5C",725,150)
BtnBox("5D",850,150)
BtnBox("4A",475,275)
BtnBox("4B",600,275)
BtnBox("4C",725,275)
BtnBox("4D",850,275)
BtnBox("3A",475,400)
BtnBox("3B",600,400)
BtnBox("3C",725,400)
BtnBox("3D",850,400)
BtnBox("2A",475,525)
BtnBox("2B",600,525)
BtnBox("2C",725,525)
BtnBox("2D",850,525)
BtnBox("1A",475,650)
BtnBox("1B",600,650)
BtnBox("1C",725,650)
BtnBox("1D",850,650)

janela.mainloop()