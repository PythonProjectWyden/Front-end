from tkinter import *

def cadastro():
    janela = Tk()
    screenRoom = Toplevel(janela)
    screenRoom.geometry("525x450")
    screenRoom.minsize(525, 450)
    screenRoom.maxsize(525, 450)
    screenRoom.title("Wyden Hotel")
    Font_tuple = ("Writer", 20, "bold")

    radio_value = IntVar()
    # Aqui estão as funçoes que aparecerem na tela de cadastro( labels e inputs)
    labelRoom = Label(screenRoom, bg="midnight blue",fg="white", width=100, height=3).pack()
    nameLabelRoom = Label(screenRoom, text="Quarto 1A:", font=("Quarto 1A:", 18), bg="midnight blue", fg="white")
    nameLabelRoom.pack()
    nameLabelRoom.configure(font=Font_tuple)
    nameLabelRoom.place(x=10, y=12)

    labelPeriod = Label(screenRoom, text="Periódo de ocupação:",font=("Periódo de ocupação:", 18))
    labelPeriod.pack()
    labelPeriod.place(x=30, y=60)

    checkInLabel = Label(screenRoom, text="Check-in:", font=("Check-in", 15))
    checkInLabel.pack()
    checkInLabel.place(x=30, y=100)

    checkInEntry = Entry(screenRoom, width=15, font=("calibri", 15))
    checkInEntry.pack()
    checkInEntry.place(x=30, y=140)

    checkOutLabel = Label(screenRoom, text="Check-out:",font=("Check-out", 15))
    checkOutLabel.pack()
    checkOutLabel.place(x=30, y=180)

    checkOutEntry = Entry(screenRoom, width=15, font=("calibri", 15))
    checkOutEntry.pack()
    checkOutEntry.place(x=30, y=220)

    nameLabel = Label(screenRoom, text="Nome do hóspede:",font=("Nome do hóspede", 15))
    nameLabel.pack()
    nameLabel.place(x=30, y=260)

    nameEntry = Entry(screenRoom, width=22, font=("calibri", 15))
    nameEntry.pack()
    nameEntry.place(x=30, y=300)

    cpfLabel = Label(screenRoom, text="CPF do hóspede:",font=("CPF do hóspede:", 15))
    cpfLabel.pack()
    cpfLabel.place(x=30, y=340)

    cpfEntry = Entry(screenRoom, width=22, font=("calibri", 15))
    cpfEntry.pack()
    cpfEntry.place(x=30, y=380)

    radiobtn1 = Radiobutton(screenRoom, text="Vago", font=("Vago", 12), variable=radio_value, value=1)
    radiobtn2 = Radiobutton(screenRoom, text="Ocupado", font=("Ocupado", 12), variable=radio_value, value=2)
    radiobtn1.pack()
    radiobtn1.place(x=380, y=130)
    radiobtn2.pack()
    radiobtn2.place(x=370, y=160)
    btnChangeColor1A = Button(screenRoom, text="SALVAR", bg="black", fg="white", width=8, height=2)
    btnChangeColor1A.pack()
    btnChangeColor1A.place(x=380, y=190)
