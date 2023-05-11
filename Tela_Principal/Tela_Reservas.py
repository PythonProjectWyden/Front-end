from tkinter import *
import tkinter as tk
from database import *
from tkcalendar import Calendar, DateEntry
from datetime import datetime 

database = RoomDB()
root = tk.Tk()
         
class tela:
    radio_value= IntVar()

    def exibir(self):
            if (self.radio_value.get() == 1):
                self.configure(bg="green")
            elif (self.radio_value.get() == 2):
                self.configure(bg="red")

    @staticmethod
    def BtnBox(quarto, x, y):
        btnBox = Button(root, text=quarto, font=(quarto, 25),bg="green", fg="white", width=5, height=2, command=lambda: tela.cadastro(quarto))
        btnBox.pack()
        btnBox.place(x=x, y=y)

    @staticmethod
    def DateBox():
        def get_dates():
            checkin = cal.selection
            checkout = cal.get_date() + " 12:00:00"
            print("Data Check-in:", checkin)
            print("Data Check-out:", checkout)
        cal = Calendar(root, mindate = datetime(2023,1,1), maxdate = datetime(2023,12,31), showweeknumbers = False, showothermonthdays = False)

        Label1 = tk.Label(root, text="Data Check-in:")
        Label1.pack()
        Label1.place(x=30,y=300)

        checkin_date = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2)
        checkin_date.pack(padx=10, pady=10)
        checkin_date.place(x=30,y=325)

        Label2 = tk.Label(root, text="Data Check-out:")
        Label2.pack()
        Label2.place(x=30,y=350)

        checkout_date = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2)
        checkout_date.pack(padx=10, pady=10)
        checkout_date.place(x=30,y=375)

        button = tk.Button(root, text="Get dates", command=get_dates)
        button.pack(pady=20)

    def Tela(): 
        root.geometry("1024x768")
        root.minsize(1024, 768)
        root.maxsize(1920, 1080)
        root.title("Tela de reservas")

        rotuloDoTitulo = Label(root, bg="dark blue", width=180, height=6)
        rotuloDoTitulo.pack()

        titulo1 = Label(root, text="Wyden Hotel", font=("Wyden Hotel", 20), bg="dark blue", fg="white",)
        titulo1.pack()
        titulo1.place(x=640, y=25)

        titulo2 = Label(root, text="Quartos:", font=("Quartos", 18))
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

        root.mainloop()

    #root DE CADASTRO/CHECK-IN

    def cadastro(quarto):
        screenRoom = Toplevel(root)
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
        
        
        
        
    