import tkinter as tk
from tkinter import *
from database import *
from tkcalendar import DateEntry
from datetime import datetime 
database = RoomDB()

checkinDentro = None
checoutDentro = None

class telasDeData:
global checkinDentro, checkoutDentro
    def proxTela():
        telasDeQuartos.segundaTela()
    
    def primeiraTela():
        global checkinDentro, checkoutDentro
        telaUm = tk.Tk()
        telaUm.geometry("300x300")
        telaUm.minsize(300, 300)
        telaUm.maxsize(300, 300)
        telaUm.title("Check-In e Check-Out")
        rotuloDoTituloTelaUm = Label(telaUm, bg="dark blue", width=180, height=6)
        rotuloDoTituloTelaUm.pack()

        tituloTelaUm1 = Label(telaUm, text="Wyden Hotel", font=("Wyden Hotel", 20), bg="dark blue", fg="white",)
        tituloTelaUm1.pack()
        tituloTelaUm1.place(x=70, y=30)

        tituloTelaUm2 = Label(telaUm, text="Datas:", font=("Datas", 18))
        tituloTelaUm2.pack()

        LabelTelaUm1 = tk.Label(telaUm, text="Data Check-in:")
        LabelTelaUm1.pack()
        LabelTelaUm1.place(x=100,y=130)

        checkin_date = DateEntry(telaUm, width=12, background='darkblue', foreground='white', borderwidth=2, mindate = datetime(2023,1,1),
                                  maxdate = datetime(2023,12,31), showweeknumbers = False, showothermonthdays = False)
        checkin_date.pack(padx=10, pady=10)
        checkin_date.place(x=100,y=150)

        LabelTelaUm2 = tk.Label(telaUm, text="Data Check-out:")
        LabelTelaUm2.pack()
        LabelTelaUm2.place(x=100,y=180)

        checkout_date = DateEntry(telaUm, width=12, background='darkblue', foreground='white', borderwidth=2, mindate = datetime(2023,1,1),
                                   maxdate = datetime(2023,12,31), showweeknumbers = False, showothermonthdays = False)
        checkout_date.pack(padx=10, pady=10)
        checkout_date.place(x=100,y=200)

        continuar = Button(telaUm,text="Salvar Datas", bg="dark blue",fg="white", width=8, height=2,command=lambda: (telasDeData.proxTela(),
                                                                                                                     telaUm.destroy()))
        continuar.pack()
        continuar.place(x=120,y=250)
        checkinDentro = checkin_date.get_date()
        checkoutDentro = checkout_date.get_date()

        telaUm.mainloop()
    
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
     global checkinDentro,checkoutDentro
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
            database.insert_room(nome,cpf,checkinDentro,checkoutDentro,quarto,1)

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
        salvarDados = Button(telaTres, text="Resumo", bg="black", fg="white", width=8, height=2, command=lambda: (save_data(), proxTela(),telaTres.destroy(), telaDois.destroy()))
        salvarDados.pack()
        salvarDados.place(x=380, y=190)
        
        def proxTela():
            TelaDeResumo.quartaTela()
            
class TelaDeResumo:
    def quartaTela():
        telaQuatro = tk.Tk()
        telaQuatro.geometry("300x300")
        telaQuatro.minsize(300, 300)
        telaQuatro.maxsize(300, 300)
        telaQuatro.title("Resumo")