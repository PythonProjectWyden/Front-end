from tkinter import *
import tkinter as tk
from database import *
from tkcalendar import Calendar
from datetime import datetime 

database = RoomDB()
janela = Tk()
calendario= Calendar(mindate = datetime(2023,1,1), maxdate = datetime(2023,12,31), showweeknumbers = False, showothermonthdays = False)
         
class tela:
    radio_value= IntVar()

    def exibir(self):
            if (self.radio_value.get() == 1):
                self.configure(bg="green")
            elif (self.radio_value.get() == 2):
                self.configure(bg="red")

    @staticmethod
    def BtnBox(quarto, x, y):
        btnBox = Button(janela, text=quarto, font=(quarto, 25),bg="green", fg="white", width=5, height=2, command=lambda: tela.cadastro(quarto))
        btnBox.pack()
        btnBox.place(x=x, y=y)

    @staticmethod
    def DateBox():
        def updateLabel():
            data = calendario.get_date()
            label.config(text="Data Selecionada: " + data)
            
        #checkOutLabel = Label(janela, text="Check-out:",font=("Check-out", 15))
        #checkOutLabel.pack()
        #checkOutLabel.place(x=30, y=180)

        #checkOutEntry = Entry(janela, width=15, font=("calibri", 15))
        #checkOutEntry.pack()
        #checkOutEntry.place(x=30, y=220)
        calendario.pack()
        calendario.place(x=30, y=100)

        calendario.bind("<<CalendarSelected>>", updateLabel)

        label = tk.Label(text="Data Selecionada: ")
        label.pack()

    def Tela(): 
        janela.geometry("1024x768")
        janela.minsize(1024, 768)
        janela.maxsize(1920, 1080)
        janela.title("Tela de reservas")

        rotuloDoTitulo = Label(janela, bg="dark blue", width=180, height=6)
        rotuloDoTitulo.pack()

        titulo1 = Label(janela, text="Wyden Hotel", font=("Wyden Hotel", 20), bg="dark blue", fg="white",)
        titulo1.pack()
        titulo1.place(x=640, y=25)

        titulo2 = Label(janela, text="Quartos:", font=("Quartos", 18))
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

        janela.mainloop()

    #JANELA DE CADASTRO/CHECK-IN

    def cadastro(quarto):
        screenRoom = Toplevel(janela)
        screenRoom.geometry("525x450")
        screenRoom.minsize(525, 450)
        screenRoom.maxsize(525, 450)
        screenRoom.title("Wyden Hotel")
        Font_tuple = ("Writer", 20, "bold")

        def save_data(data):
            nome = nameEntry.get()
            cpf = cpfEntry.get()
            checkin = data
            checkout = data
            database.insert_room(checkin,checkout,nome,1,cpf,quarto)
            screenRoom.destroy()

        radio_value = IntVar()
        # Aqui estão as funçoes que aparecerem na tela de cadastro( labels e inputs)
        labelRoom = Label(screenRoom, bg="midnight blue",fg="white", width=100, height=3).pack()
        
        nameLabelRoom = Label(screenRoom, text="quarto: "+quarto, bg="midnight blue", fg="white")
        nameLabelRoom.pack()
        nameLabelRoom.configure(font=Font_tuple)
        nameLabelRoom.place(x=10, y=12)

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
        btnChangeColor1A = Button(screenRoom, text="SALVAR", bg="black", fg="white", width=8, height=2, command=lambda: save_data())
        btnChangeColor1A.pack()
        btnChangeColor1A.place(x=380, y=190)
        
        
        
        
    