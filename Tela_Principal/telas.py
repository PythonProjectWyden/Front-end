from tkinter import *
import tkinter as tk
from database import *
from tkcalendar import Calendar, DateEntry
from datetime import datetime 

class telas:
    telaUm = tk.Tk()
    telaUm.geometry("300x300")
    telaUm.minsize(300, 300)
    telaUm.maxsize(300, 300)
    telaUm.title("Tela Check-In e Check-Out")
    rotuloDoTituloTelaUm = Label(telaUm, bg="dark blue", width=180, height=6)
    rotuloDoTituloTelaUm.pack()

    tituloTelaUm1 = Label(telaUm, text="Wyden Hotel", font=("Wyden Hotel", 20), bg="dark blue", fg="white",)
    tituloTelaUm1.pack()
    tituloTelaUm1.place(x=640, y=25)

    tituloTelaUm2 = Label(telaUm, text="Datas:", font=("Datas", 18))
    tituloTelaUm2.pack()


    teladois = tk.Tk()
    teladois.geometry("1024x768")
    teladois.minsize(1024, 768)
    teladois.maxsize(1920, 1080)
    teladois.title("Tela de reservas")

    rotuloDoTitulo = Label(teladois, bg="dark blue", width=180, height=6)
    rotuloDoTitulo.pack()

    titulo1 = Label(teladois, text="Wyden Hotel", font=("Wyden Hotel", 20), bg="dark blue", fg="white",)
    titulo1.pack()
    titulo1.place(x=640, y=25)

    titulo2 = Label(teladois, text="Quartos:", font=("Quartos", 18))
    titulo2.pack()