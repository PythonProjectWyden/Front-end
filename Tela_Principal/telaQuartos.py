from tkinter import *
import tkinter as tk
from database import *
import telaResumo
database = RoomDB()

telaDois = None
Quarto = None

class telasDeQuartos:

    def segundaTela():
        global telaDois
        teladois = tk.Tk()
        telaDois = teladois
        telaDois.geometry("1024x768")
        telaDois.minsize(1024, 768)
        telaDois.maxsize(1920, 1080)
        telaDois.title("Tela de reservas")
        rotuloDoTitulo = Label(telaDois, bg="dark blue", width=180, height=6)
        rotuloDoTitulo.pack()

        titulo1 = Label(telaDois, text="Wyden Hotel", font=("Wyden Hotel", 20), bg="dark blue", fg="white",)
        titulo1.pack()
        titulo1.place(x=430,y=30)

        titulo2 = Label(telaDois, text="Quartos:", font=("Quartos", 18))
        titulo2.pack()

        telasDeQuartos.BtnBox("5A", 475, 150)
        telasDeQuartos.BtnBox("5B", 600, 150)
        telasDeQuartos.BtnBox("5C", 725, 150)
        telasDeQuartos.BtnBox("5D", 850, 150)
        telasDeQuartos.BtnBox("4A", 475, 275)
        telasDeQuartos.BtnBox("4B", 600, 275)
        telasDeQuartos.BtnBox("4C", 725, 275)
        telasDeQuartos.BtnBox("4D", 850, 275)
        telasDeQuartos.BtnBox("3A", 475, 400)
        telasDeQuartos.BtnBox("3B", 600, 400)
        telasDeQuartos.BtnBox("3C", 725, 400)
        telasDeQuartos.BtnBox("3D", 850, 400)
        telasDeQuartos.BtnBox("2A", 475, 525)
        telasDeQuartos.BtnBox("2B", 600, 525)
        telasDeQuartos.BtnBox("2C", 725, 525)
        telasDeQuartos.BtnBox("2D", 850, 525)
        telasDeQuartos.BtnBox("1A", 475, 650)
        telasDeQuartos.BtnBox("1B", 600, 650)
        telasDeQuartos.BtnBox("1C", 725, 650)
        telasDeQuartos.BtnBox("1D", 850, 650)
    
    @staticmethod
    def BtnBox(quarto, x, y,):
            btnBox = Button(telaDois, text=quarto, font=(quarto, 25), bg="green", fg="white", width=5, height=2, command=lambda:Cadastro.cadastro(quarto))
            btnBox.pack()
            btnBox.place(x=x, y=y)

class Cadastro:
     def cadastro(quarto):
        telaTres = tk.Tk()
        telaTres.geometry("525x450")
        telaTres.minsize(525, 450)
        telaTres.maxsize(525, 450)
        telaTres.title("Wyden Hotel")
        Font_tuple = ("Writer", 20, "bold")

        def save_data():
            nome = nameEntry.get()
            cpf = cpfEntry.get()
            database.insert_room(nome,cpf,quarto,1)

        rotuloDoTitulo = Label(telaTres, bg="dark blue", width=180, height=6)
        rotuloDoTitulo.pack()
            
        nameLabelRoom = Label(telaTres, text="quarto:"+quarto ,bg="dark blue" ,fg="white")
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
        salvarDados = Button(telaTres, text="Resumo", bg="black", fg="white", width=8, height=2, command=lambda: (save_data(), proxTela(),
                                                                                                                   telaTres.destroy(), telaDois.destroy()))
        salvarDados.pack()
        salvarDados.place(x=380, y=190)

        def proxTela():
            telaResumo.TelaDeResumo.quartaTela()