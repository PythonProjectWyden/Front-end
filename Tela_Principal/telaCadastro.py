from tkinter import *
import tkinter as tk
from database import *
from telaData import telasDeData
import telaResumo
database = RoomDB()

def cadastro(Quarto):
    telaTres = tk.Tk()
    telaTres.geometry("525x450")
    telaTres.minsize(525, 450)
    telaTres.maxsize(525, 450)
    telaTres.title("Wyden Hotel")
    Font_tuple = ("Writer", 20, "bold")

    def save_data():
        checkin = telasDeData.primeiraTela
        checkout = telasDeData.returnCheckout()
        nome = nameEntry.get()
        cpf = cpfEntry.get()
        database.insert_room(nome,cpf,str(Quarto),1)
        database.insert_checks(checkin,checkout,cpf)


    rotuloDoTitulo = Label(telaTres, bg="dark blue", width=180, height=6)
    rotuloDoTitulo.pack()
        
    nameLabelRoom = Label(telaTres, text="quarto:"+str(Quarto) ,bg="dark blue" ,fg="white")
    nameLabelRoom.pack()
    nameLabelRoom.configure(font=Font_tuple)
    nameLabelRoom.place(x=10, y=30)

    nameLabel = Label(telaTres, text="Nome do hóspede:",font=("Nome do hóspede", 15))
    nameLabel.pack()
    nameLabel.place(x=30, y=100)

    nameEntry = Entry(telaTres, width=22, font=("calibri", 15))
    nameEntry.pack()
    nameEntry.place(x=30, y=140)

    cpfLabel = Label(telaTres, text="CPF do hóspede:",font=("CPF do hóspede:", 15))
    cpfLabel.pack()
    cpfLabel.place(x=30, y=180)
    cpfEntry = Entry(telaTres, width=22, font=("calibri", 15))
    cpfEntry.pack()
    cpfEntry.place(x=30, y=220)
    salvarDados = Button(telaTres, text="Resumo", bg="black", fg="white", width=8, height=2, command=lambda: (save_data(), proxTela()))
    salvarDados.pack()
    salvarDados.place(x=380, y=190)

    def proxTela():
        telaResumo.TelaDeResumo.quartaTela()
