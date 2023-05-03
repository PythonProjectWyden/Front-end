from tkinter import *
from tkinter import ttk
from tkinter import messagebox

janela = Tk()
janela.geometry("1024x720")
janela.minsize(1024, 700)
janela.maxsize(1920,1060)

janela.title("Tela de reservas")

rotuloDoTitulo = Label(janela, bg="dark blue", width=180, height=6)
rotuloDoTitulo.pack()

titulo1 = Label(janela, text="Wyden Hotel", font=("Wyden Hotel", 20), bg="dark blue", fg="white")
titulo1.pack()
titulo1.place(x=640, y=25)

titulo2 = Label(janela, text="Quartos:", font=("Quartos", 18))  
titulo2.pack()
#----------------------------------------------------------------------------------------------
#Esses são os contadores das páginas abertas
global Quarto
Quarto = 1

#Essa é a função que abre a nova janela de cadastro dos quartos, cada quarto tem sua função. 
#Ela se repete em todos os quartos, só se altera a variável.
def windowRoom(): 
  global Quarto
  #essa função que muda a cor do botão na tela principal.
  def exibir():
    if(radio_value.get() == 1):
          btnBox.configure(bg="green")
    elif(radio_value.get() == 2):
          btnBox.configure(bg="red")
  #Esse if  que faz a contagem das abas abertas
  if Quarto < 2:
    #Essa função que faz abrir o calendário quando clica pra escolher as datas ( você precisa instalar o tk calendar)
    #Ela está na data de Check in e Check out
    def pick_date(event):
      global cal, date_window
      
      date_window =Toplevel()
      date_window.grab_set()
      date_window.title("Escolha uma data de check-in")
      date_window.geometry('250x220+590+370')
      cal=Calendar(date_window, selectmode="day" ,date_pattern="dd/mm/y")
      cal.place(x=0 ,y=0)
      
      submit_btn=Button(date_window,text="confimar",command=grab_date)
      submit_btn.place(x=80,y=190)
      
    def grab_date():
        
        checkInEntry.delete(0,END)
        checkInEntry.insert(0,cal.get_date())
        date_window.destroy()
        
    def pick_dateout(event):
        global cal, date_window
        
        date_window =Toplevel()
        date_window.grab_set()
        date_window.title("Escolha uma data de check-out")
        date_window.geometry('250x220+590+370')
        cal=Calendar(date_window, selectmode="day" ,date_pattern="dd/mm/y")
        cal.place(x=0 ,y=0)
        
        submit_btn=Button(date_window,text="confimar",command=grab_dateout)
        submit_btn.place(x=80,y=190)
        
    def grab_dateout():
        
        checkOutEntry.delete(0,END)
        checkOutEntry.insert(0,cal.get_date())
        date_window.destroy()
        
    screenRoom = Toplevel(janela)
    screenRoom.geometry("525x450")
    screenRoom.minsize(525,450)
    screenRoom.maxsize(525,450)
    screenRoom.title("Wyden Hotel")
    Font_tuple = ("Writer", 20, "bold")

    radio_value=IntVar() 
    #Aqui estão as funçoes que aparecerem na tela de cadastro( labels e inputs)
    labelRoom = Label(screenRoom, bg="midnight blue",fg="white", width= 100, height=3).pack()
    nameLabelRoom = Label(screenRoom, text="Quarto 1A:", font=("Quarto 1A:", 18), bg="midnight blue", fg="white")
    nameLabelRoom.pack()
    nameLabelRoom.configure(font=Font_tuple)
    nameLabelRoom.place(x=10, y=12)

    labelPeriod = Label(screenRoom, text="Periódo de ocupação:", font=("Periódo de ocupação:", 18))
    labelPeriod.pack()
    labelPeriod.place(x=30, y=60)

    checkInLabel = Label(screenRoom, text="Check-in:", font=("Check-in", 15))
    checkInLabel.pack()
    checkInLabel.place(x=30, y=100)

    checkInEntry = Entry(screenRoom, width=15, font=("calibri", 15))
    checkInEntry.pack()
    checkInEntry.place(x=30, y=140)
    checkInEntry.bind("<1>", pick_date)

    checkOutLabel = Label(screenRoom, text="Check-out:", font=("Check-out", 15))
    checkOutLabel.pack()
    checkOutLabel.place(x=30, y=180)

    checkOutEntry = Entry(screenRoom, width=15, font=("calibri", 15))
    checkOutEntry.pack()
    checkOutEntry.place(x=30, y=220)
    checkOutEntry.bind("<1>", pick_dateout)

    nameLabel = Label(screenRoom, text="Nome do hóspede:", font=("Nome do hóspede", 15))
    nameLabel.pack()
    nameLabel.place(x=30, y=260)

    nameEntry = Entry(screenRoom, width=22, font=("calibri", 15))
    nameEntry.pack()
    nameEntry.place(x=30, y=300)

    cpfLabel = Label(screenRoom, text="CPF do hóspede:", font=("CPF do hóspede:", 15))
    cpfLabel.pack()
    cpfLabel.place(x=30, y=340)

    cpfEntry = Entry(screenRoom, width=22, font=("calibri", 15))
    cpfEntry.pack()
    cpfEntry.place(x=30, y=380)

    radiobtn1 = Radiobutton(screenRoom, text="Vago", font=("Vago", 12), variable=radio_value, value=1)
    radiobtn2 = Radiobutton(screenRoom, text="Ocupado",font=("Ocupado", 12), variable=radio_value, value=2)
    radiobtn1.pack()
    radiobtn1.place(x=380, y=130)
    radiobtn2.pack()
    radiobtn2.place(x=370, y=160)
    btnChangeColor1A = Button(screenRoom, text="SALVAR", bg="black", fg="white", width=8, height=2, command=exibir)
    btnChangeColor1A.pack()
    btnChangeColor1A.place(x=380, y=190)

    
  else:
    #essa é uma função de aparecer uma menssage box quando tentamos abrir a mesma janela mais de uma vez
    #ainda está bugada
    messagebox.showinfo("Error","A janela do quarto {} já está aberta!".format() )
#E essas funcões irão se repetir em todos os quartos, mas ainda está incompleto
#Vamos implementar as funções que o professor aconselho e tentar colocar orientação a objetos

#Aqui estão todos os botões da tela principal
#Tentaremos colocar a função de criar novos botões de forma mais fácil.

btnBox = Button(janela, text="5A", font=("5A", 25), bg="green", fg="white", width=5, height=2, command=windowRoom)
btnBox.pack()
btnBox.place(x=475, y=150)

btnBox = Button(janela, text="5B", font=("5B", 25), bg="green", fg="white", width=5, height=2, command=windowRoom)
btnBox.pack()
btnBox.place(x=600, y=150)

btnBox = Button(janela, text="5C", font=("5C", 25), bg="green", fg="white", width=5, height=2, command=windowRoom)
btnBox.pack()
btnBox.place(x=725, y=150)

btnBox = Button(janela, text="5D", font=("5D", 25), bg="green", fg="white", width=5, height=2, command=windowRoom)
btnBox.pack()
btnBox.place(x=850, y=150)

btnBox = Button(janela, text="4A", font=("4A", 25), bg="green", fg="white", width=5, height=2, command=windowRoom)
btnBox.pack()
btnBox.place(x=475, y=275)

btnBox = Button(janela, text="4B", font=("4B", 25), bg="green", fg="white", width=5, height=2, command=windowRoom)
btnBox.pack()
btnBox.place(x=600, y=275)

btnBox = Button(janela, text="4C", font=("4C", 25), bg="green", fg="white", width=5, height=2, command=windowRoom)
btnBox.pack()
btnBox.place(x=725, y=275)

btnBox = Button(janela, text="4D", font=("4D", 25), bg="green", fg="white", width=5, height=2, command=windowRoom)
btnBox.pack()
btnBox.place(x=850, y=275)

btnBox3A = Button(janela, text="3A", font=("3A", 25), bg="green", fg="white", width=5, height=2, command=windowRoom)
btnBox3A.pack()
btnBox3A.place(x=475, y=400)

btnBox3B = Button(janela, text="3B", font=("3B", 25), bg="green", fg="white", width=5, height=2, command=windowRoom)
btnBox3B.pack()
btnBox3B.place(x=600, y=400)

btnBox = Button(janela, text="3C", font=("3C", 25), bg="green", fg="white", width=5, height=2, command=windowRoom)
btnBox.pack()
btnBox.place(x=725, y=400)

btnBox = Button(janela, text="3D", font=("3D", 25), bg="green", fg="white", width=5, height=2, command=windowRoom)
btnBox.pack()
btnBox.place(x=850, y=400)

btnBox = Button(janela, text="2A", font=("2A", 25), bg="green", fg="white", width=5, height=2, command=windowRoom)
btnBox.pack()
btnBox.place(x=475, y=525)

btnBox = Button(janela, text="2B", font=("2B", 25), bg="green", fg="white", width=5, height=2, command=windowRoom)
btnBox.pack()
btnBox.place(x=600, y=525)

btnBox = Button(janela, text="2C", font=("2C", 25), bg="green", fg="white", width=5, height=2, command=windowRoom)
btnBox.pack()
btnBox.place(x=725, y=525)

btnBox = Button(janela, text="2D", font=("2D", 25), bg="green", fg="white", width=5, height=2, command=windowRoom)
btnBox.pack()
btnBox.place(x=850, y=525)

btnBox = Button(janela, text="1A", font=("1A", 25), bg="green", fg="white", width=5, height=2, command=windowRoom)
btnBox.pack()
btnBox.place(x=475, y=650)

btnBox = Button(janela, text="1B", font=("1B", 25), bg="green", fg="white", width=5, height=2, command=windowRoom)
btnBox.pack()
btnBox.place(x=600, y=650)

btnBox = Button(janela, text="1C", font=("1C", 25), bg="green", fg="white", width=5, height=2, command=windowRoom)
btnBox.pack()
btnBox.place(x=725, y=650)

btnBox = Button(janela, text="1D", font=("1D", 25), bg="green", fg="white", width=5, height=2, command=windowRoom)
btnBox.pack()
btnBox.place(x=850, y=650)

janela.mainloop()