from tkinter import *
import tkinter as tk
from database import *
from tkcalendar import Calendar, DateEntry
from datetime import datetime 
from telas import *

database = RoomDB()
         
class tela:
    checkin = checkout = checkindate = checkoutdate = None
    radio_value= IntVar()


    @staticmethod
    def DateBox():

        def update_checkin_date(date):
            tela.checkindate = date

        def update_checkout_date(date):
            tela.checkoutdate = date

        Label1 = tk.Label(telas.telaUm, text="Data Check-in:")
        Label1.pack()
        Label1.place(x=30,y=100)

        checkin_date = DateEntry(telas.telaUm, width=12, background='darkblue', foreground='white', borderwidth=2, mindate = datetime(2023,1,1), maxdate = datetime(2023,12,31), showweeknumbers = False, showothermonthdays = False, command=update_checkin_date)
        checkin_date.pack(padx=10, pady=10)
        checkin_date.place(x=30,y=125)
        tela.checkindate = checkin_date.get_date()

        Label2 = tk.Label(telas.telaUm, text="Data Check-out:")
        Label2.pack()
        Label2.place(x=30,y=150)

        checkout_date = DateEntry(telas.telaUm, width=12, background='darkblue', foreground='white', borderwidth=2, mindate = datetime(2023,1,1), maxdate = datetime(2023,12,31), showweeknumbers = False, showothermonthdays = False, command=update_checkout_date)
        checkout_date.pack(padx=10, pady=10)
        checkout_date.place(x=30,y=175)
        tela.checkoutdate = checkout_date.get_date()

    @staticmethod
    def BtnBox(quarto, x, y):
        btnBox = Button(telas.teladois, text=quarto, font=(quarto, 25),bg="green", fg="white", width=5, height=2, command=lambda: tela.cadastro(quarto))
        btnBox.pack()
        btnBox.place(x=x, y=y)

    def Tela():

        rotuloDoTitulo = Label(telas.teladois, bg="dark blue", width=180, height=6)
        rotuloDoTitulo.pack()

        titulo1 = Label(telas.teladois, text="Wyden Hotel", font=("Wyden Hotel", 20), bg="dark blue", fg="white",)
        titulo1.pack()
        titulo1.place(x=640, y=25)

        titulo2 = Label(telas.teladois, text="Quartos:", font=("Quartos", 18))
        titulo2.pack()

        tela.DateBox()
        tela.BtnBox("5A", 475, 150)
        tela.BtnBox("5B", 600, 150)
        tela.BtnBox("5C", 725, 150)
        tela.BtnBox("5D", 850, 150)
        tela.BtnBox("4A", 475, 275)
        tela.BtnBox("4B", 600, 275)
        tela.BtnBox("4C", 725, 275)
        tela.BtnBox("4D", 850, 275)
        tela.BtnBox("3A", 475, 400)
        tela.BtnBox("3B", 600, 400)
        tela.BtnBox("3C", 725, 400)
        tela.BtnBox("3D", 850, 400)
        tela.BtnBox("2A", 475, 525)
        tela.BtnBox("2B", 600, 525)
        tela.BtnBox("2C", 725, 525)
        tela.BtnBox("2D", 850, 525)
        tela.BtnBox("1A", 475, 650)
        tela.BtnBox("1B", 600, 650)
        tela.BtnBox("1C", 725, 650)
        tela.BtnBox("1D", 850, 650)

        telas.telaUm.mainloop()

    #telas.teladois DE CADASTRO/CHECK-IN

    def cadastro(quarto):
        screenRoom = Toplevel(telas.teladois)
        screenRoom.geometry("525x450")
        screenRoom.minsize(525, 450)
        screenRoom.maxsize(525, 450)
        screenRoom.title("Wyden Hotel")
        Font_tuple = ("Writer", 20, "bold")

        def save_data():
            nome = nameEntry.get()
            cpf = cpfEntry.get()
            database.insert_room(nome, cpf, quarto, 1)
            checkin = tela.checkindate
            checkout = tela.checkoutdate
            database.insert_checks(checkin, checkout, 1)
            screenRoom.destroy()
            telas.teladois.destroy()


        rotuloDoTitulo = Label(screenRoom, bg="dark blue", width=180, height=6)
        rotuloDoTitulo.pack()
         
        nameLabelRoom = Label(screenRoom, text="quarto: "+quarto,bg="dark blue" ,fg="white")
        nameLabelRoom.pack()
        nameLabelRoom.configure(font=Font_tuple)
        nameLabelRoom.place(x=10, y=30)

        nameLabel = Label(screenRoom, text="Nome do hóspede:",font=("Nome do hóspede", 15))
        nameLabel.pack()
        nameLabel.place(x=30, y=100)

        nameEntry = Entry(screenRoom, width=22, font=("calibri", 15))
        nameEntry.pack()
        nameEntry.place(x=30, y=140)

        cpfLabel = Label(screenRoom, text="CPF do hóspede:",font=("CPF do hóspede:", 15))
        cpfLabel.pack()
        cpfLabel.place(x=30, y=180)
        cpfEntry = Entry(screenRoom, width=22, font=("calibri", 15))
        cpfEntry.pack()
        cpfEntry.place(x=30, y=220)
        salvarDados = Button(screenRoom, text="SALVAR", bg="black", fg="white", width=8, height=2, command=lambda: save_data())
        salvarDados.pack()
        salvarDados.place(x=380, y=190)
    