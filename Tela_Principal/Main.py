<<<<<<< Updated upstream
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import*

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
global counter5A, counter5B, counter5C, counter5D, counter4A, counter4B, counter4C, counter4D, counter3A, counter3B
global counter3C, counter3D, counter2A, counter2B, counter2C, counter2D, counter1A, counter1B, counter1C, counter1D
counter5A = 1
counter5B = 1
counter5C = 1
counter5D = 1
counter4A = 1
counter4B = 1
counter4C = 1
counter4D = 1
counter3A = 1
counter3B = 1
counter3C = 1
counter3D = 1
counter2A = 1
counter2B = 1
counter2C = 1
counter2D = 1
counter1A = 1
counter1B = 1
counter1C = 1
counter1D = 1
#Essa é a função que abre a nova janela de cadastro dos quartos, cada quarto tem sua função. 
#Ela se repete em todos os quartos, só se altera a variável.
def windowRoom5A(): 
  global counter5A
  #essa função que muda a cor do botão na tela principal.
  def exibir5A():
    if(radio_value.get() == 1):
          btnBox5A.configure(bg="green")
    elif(radio_value.get() == 2):
          btnBox5A.configure(bg="red")
  #Esse if  que faz a contagem das abas abertas
  if counter5A < 2:
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
        
    screenRoom5A = Toplevel(janela)
    screenRoom5A.geometry("525x450")
    screenRoom5A.minsize(525,450)
    screenRoom5A.maxsize(525,450)
    screenRoom5A.title("Wyden Hotel")
    Font_tuple = ("Writer", 20, "bold")

    radio_value=IntVar() 
    #Aqui estão as funçoes que aparecerem na tela de cadastro( labels e inputs)
    labelRoom = Label(screenRoom5A, bg="midnight blue",fg="white", width= 100, height=3).pack()
    nameLabelRoom = Label(screenRoom5A, text="Quarto 1A:", font=("Quarto 1A:", 18), bg="midnight blue", fg="white")
    nameLabelRoom.pack()
    nameLabelRoom.configure(font=Font_tuple)
    nameLabelRoom.place(x=10, y=12)

    labelPeriod = Label(screenRoom5A, text="Periódo de ocupação:", font=("Periódo de ocupação:", 18))
    labelPeriod.pack()
    labelPeriod.place(x=30, y=60)

    checkInLabel = Label(screenRoom5A, text="Check-in:", font=("Check-in", 15))
    checkInLabel.pack()
    checkInLabel.place(x=30, y=100)

    checkInEntry = Entry(screenRoom5A, width=15, font=("calibri", 15))
    checkInEntry.pack()
    checkInEntry.place(x=30, y=140)
    checkInEntry.bind("<1>", pick_date)

    checkOutLabel = Label(screenRoom5A, text="Check-out:", font=("Check-out", 15))
    checkOutLabel.pack()
    checkOutLabel.place(x=30, y=180)

    checkOutEntry = Entry(screenRoom5A, width=15, font=("calibri", 15))
    checkOutEntry.pack()
    checkOutEntry.place(x=30, y=220)
    checkOutEntry.bind("<1>", pick_dateout)

    nameLabel = Label(screenRoom5A, text="Nome do hóspede:", font=("Nome do hóspede", 15))
    nameLabel.pack()
    nameLabel.place(x=30, y=260)

    nameEntry = Entry(screenRoom5A, width=22, font=("calibri", 15))
    nameEntry.pack()
    nameEntry.place(x=30, y=300)

    cpfLabel = Label(screenRoom5A, text="CPF do hóspede:", font=("CPF do hóspede:", 15))
    cpfLabel.pack()
    cpfLabel.place(x=30, y=340)

    cpfEntry = Entry(screenRoom5A, width=22, font=("calibri", 15))
    cpfEntry.pack()
    cpfEntry.place(x=30, y=380)

    radiobtn1 = Radiobutton(screenRoom5A, text="Vago", font=("Vago", 12), variable=radio_value, value=1)
    radiobtn2 = Radiobutton(screenRoom5A, text="Ocupado",font=("Ocupado", 12), variable=radio_value, value=2)
    radiobtn1.pack()
    radiobtn1.place(x=380, y=130)
    radiobtn2.pack()
    radiobtn2.place(x=370, y=160)
    btnChangeColor1A = Button(screenRoom5A, text="SALVAR", bg="black", fg="white", width=8, height=2, command=exibir5A)
    btnChangeColor1A.pack()
    btnChangeColor1A.place(x=380, y=190)

    counter5A +=1
  else:
    #essa é uma função de aparecer uma menssage box quando tentamos abrir a mesma janela mais de uma vez
    #ainda está bugada
    messagebox.showinfo("Error","A janela do quarto 5A já está aberta!" )
#E essas funcões irão se repetir em todos os quartos, mas ainda está incompleto
#Vamos implementar as funções que o professor aconselho e tentar colocar orientação a objetos
def windowRoom5B():
    global counter5B
    def exibir5B():
      if(radio_value.get() == 1):
        btnBox5B.configure(bg="green")
      elif(radio_value.get() == 2):
        btnBox5B.configure(bg="red")

    if counter5B < 2: 
      screenRoom5B = Toplevel(janela)
      screenRoom5B.title("Quarto 5B")
      screenRoom5B.geometry("400x400")
      
      Label(screenRoom5B,
            text ="This is a new window").pack()
      radio_value=IntVar()
      
      radiobtn1 = Radiobutton(screenRoom5B, text="Vago", variable=radio_value, value=1)
      radiobtn2 = Radiobutton(screenRoom5B, text="Ocupado", variable=radio_value, value=2)
      radiobtn1.pack()
      radiobtn2.pack()
      
      btnChangeColor5B = Button(screenRoom5B, text="Escolher", bg="black", fg="white", width=7, height=2, command= exibir5B)
      btnChangeColor5B.pack()
      counter5B +=1
    else:
      messagebox.showinfo("Error","A janela do quarto 5B já está aberta!")
      
def windowRoom5C():
    global counter5C
    def exibir5C():
      if(radio_value.get() == 1):
        btnBox5C.configure(bg="green")
      elif(radio_value.get() == 2):
        btnBox5C.configure(bg="red")

    if counter5C < 2: 
      screenRoom5C = Toplevel(janela)
      screenRoom5C.title("Quarto 5C")
      screenRoom5C.geometry("400x400")
      
      Label(screenRoom5C,
            text ="This is a new window").pack()
      radio_value=IntVar()
      
      radiobtn1 = Radiobutton(screenRoom5C, text="Vago", variable=radio_value, value=1)
      radiobtn2 = Radiobutton(screenRoom5C, text="Ocupado", variable=radio_value, value=2)
      radiobtn1.pack()
      radiobtn2.pack()
      
      btnChangeColor5C = Button(screenRoom5C, text="Escolher", bg="black", fg="white", width=7, height=2, command= exibir5C)
      btnChangeColor5C.pack()
      counter5C +=1
    else:
      messagebox.showinfo("Error","A janela do quarto 5C já está aberta!")
    
def windowRoom5D():
    global counter5D
    def exibir5D():
      if(radio_value.get() == 1):
        btnBox5D.configure(bg="green")
      elif(radio_value.get() == 2):
        btnBox5D.configure(bg="red")

    if counter5D < 2: 
      screenRoom5D = Toplevel(janela)
      screenRoom5D.title("Quarto 5D")
      screenRoom5D.geometry("400x400")
      
      Label(screenRoom5D,
            text ="This is a new window").pack()
      radio_value=IntVar()
      
      radiobtn1 = Radiobutton(screenRoom5D, text="Vago", variable=radio_value, value=1)
      radiobtn2 = Radiobutton(screenRoom5D, text="Ocupado", variable=radio_value, value=2)
      radiobtn1.pack()
      radiobtn2.pack()
      
      btnChangeColor5D = Button(screenRoom5D, text="Escolher", bg="black", fg="white", width=7, height=2, command= exibir5D)
      btnChangeColor5D.pack()
      counter5D +=1
    else:
      messagebox.showinfo("Error","A janela do quarto 5D já está aberta!")

def windowRoom4A():
    global counter4A
    def exibir4A():
      if(radio_value.get() == 1):
        btnBox4A.configure(bg="green")
      elif(radio_value.get() == 2):
        btnBox4A.configure(bg="red")

    if counter4A < 2: 
      screenRoom4A = Toplevel(janela)
      screenRoom4A.title("Quarto 4A")
      screenRoom4A.geometry("400x400")
      
      Label(screenRoom4A,
            text ="This is a new window").pack()
      radio_value=IntVar()
      
      radiobtn1 = Radiobutton(screenRoom4A, text="Vago", variable=radio_value, value=1)
      radiobtn2 = Radiobutton(screenRoom4A, text="Ocupado", variable=radio_value, value=2)
      radiobtn1.pack()
      radiobtn2.pack()
      
      btnChangeColor4A = Button(screenRoom4A, text="Escolher", bg="black", fg="white", width=7, height=2, command= exibir4A)
      btnChangeColor4A.pack()
      counter4A +=1
    else:
      messagebox.showinfo("Error","A janela do quarto 4A já está aberta!")

def windowRoom4B():
    global counter4B
    def exibir4B():
      if(radio_value.get() == 1):
        btnBox4B.configure(bg="green")
      elif(radio_value.get() == 2):
        btnBox4B.configure(bg="red")

    if counter4B < 2: 
      screenRoom4B = Toplevel(janela)
      screenRoom4B.title("Quarto 4B")
      screenRoom4B.geometry("400x400")
      
      Label(screenRoom4B,
            text ="This is a new window").pack()
      radio_value=IntVar()
      
      radiobtn1 = Radiobutton(screenRoom4B, text="Vago", variable=radio_value, value=1)
      radiobtn2 = Radiobutton(screenRoom4B, text="Ocupado", variable=radio_value, value=2)
      radiobtn1.pack()
      radiobtn2.pack()
      
      btnChangeColor4B = Button(screenRoom4B, text="Escolher", bg="black", fg="white", width=7, height=2, command= exibir4B)
      btnChangeColor4B.pack()
      counter4B +=1
    else:
      messagebox.showinfo("Error","A janela do quarto 4B já está aberta!")

def windowRoom4C():
    global counter4C
    def exibir4C():
      if(radio_value.get() == 1):
        btnBox4C.configure(bg="green")
      elif(radio_value.get() == 2):
        btnBox4C.configure(bg="red")

    if counter4C < 2: 
      screenRoom4C = Toplevel(janela)
      screenRoom4C.title("Quarto 4C")
      screenRoom4C.geometry("400x400")
      
      Label(screenRoom4C,
            text ="This is a new window").pack()
      radio_value=IntVar()
      
      radiobtn1 = Radiobutton(screenRoom4C, text="Vago", variable=radio_value, value=1)
      radiobtn2 = Radiobutton(screenRoom4C, text="Ocupado", variable=radio_value, value=2)
      radiobtn1.pack()
      radiobtn2.pack()
      
      btnChangeColor4C = Button(screenRoom4C, text="Escolher", bg="black", fg="white", width=7, height=2, command= exibir4C)
      btnChangeColor4C.pack()
      counter4C +=1
    else:
      messagebox.showinfo("Error","A janela do quarto 4C já está aberta!")

def windowRoom4D():
    global counter4D
    def exibir4D():
      if(radio_value.get() == 1):
        btnBox4D.configure(bg="green")
      elif(radio_value.get() == 2):
        btnBox4D.configure(bg="red")

    if counter4D < 2: 
      screenRoom4D = Toplevel(janela)
      screenRoom4D.title("Quarto 4D")
      screenRoom4D.geometry("400x400")
      
      Label(screenRoom4D,
            text ="This is a new window").pack()
      radio_value=IntVar()
      
      radiobtn1 = Radiobutton(screenRoom4D, text="Vago", variable=radio_value, value=1)
      radiobtn2 = Radiobutton(screenRoom4D, text="Ocupado", variable=radio_value, value=2)
      radiobtn1.pack()
      radiobtn2.pack()
      
      btnChangeColor4D = Button(screenRoom4D, text="Escolher", bg="black", fg="white", width=7, height=2, command= exibir4D)
      btnChangeColor4D.pack()
      counter4D +=1
    else:
      messagebox.showinfo("Error","A janela do quarto 4D já está aberta!")

def windowRoom3A():
    global counter3A
    def exibir3A():
      if(radio_value.get() == 1):
        btnBox3A.configure(bg="green")
      elif(radio_value.get() == 2):
        btnBox3A.configure(bg="red")

    if counter3A < 2: 
      screenRoom3A = Toplevel(janela)
      screenRoom3A.title("Quarto 3A")
      screenRoom3A.geometry("400x400")
      
      Label(screenRoom3A,
            text ="This is a new window").pack()
      radio_value=IntVar()
      
      radiobtn1 = Radiobutton(screenRoom3A, text="Vago", variable=radio_value, value=1)
      radiobtn2 = Radiobutton(screenRoom3A, text="Ocupado", variable=radio_value, value=2)
      radiobtn1.pack()
      radiobtn2.pack()
      
      btnChangeColor3A = Button(screenRoom3A, text="Escolher", bg="black", fg="white", width=7, height=2, command= exibir3A)
      btnChangeColor3A.pack()
      counter3A +=1
    else:
      messagebox.showinfo("Error","A janela do quarto 3A já está aberta!")

def windowRoom3B():
    global counter3B
    def exibir3B():
      if(radio_value.get() == 1):
        btnBox3B.configure(bg="green")
      elif(radio_value.get() == 2):
        btnBox3B.configure(bg="red")

    if counter3B < 2: 
      screenRoom3B = Toplevel(janela)
      screenRoom3B.title("Quarto 3B")
      screenRoom3B.geometry("400x400")
      
      Label(screenRoom3B,
            text ="This is a new window").pack()
      radio_value=IntVar()
      
      radiobtn1 = Radiobutton(screenRoom3B, text="Vago", variable=radio_value, value=1)
      radiobtn2 = Radiobutton(screenRoom3B, text="Ocupado", variable=radio_value, value=2)
      radiobtn1.pack()
      radiobtn2.pack()
      
      btnChangeColor3B = Button(screenRoom3B, text="Escolher", bg="black", fg="white", width=7, height=2, command= exibir3B)
      btnChangeColor3B.pack()
      counter3B +=1
    else:
      messagebox.showinfo("Error","A janela do quarto 3B já está aberta!")

def windowRoom3C():
    global counter3C
    def exibir3C():
      if(radio_value.get() == 1):
        btnBox3C.configure(bg="green")
      elif(radio_value.get() == 2):
        btnBox3C.configure(bg="red")

    if counter3C < 2: 
      screenRoom3C = Toplevel(janela)
      screenRoom3C.title("Quarto 3C")
      screenRoom3C.geometry("400x400")
      
      Label(screenRoom3C,
            text ="This is a new window").pack()
      radio_value=IntVar()
      
      radiobtn1 = Radiobutton(screenRoom3C, text="Vago", variable=radio_value, value=1)
      radiobtn2 = Radiobutton(screenRoom3C, text="Ocupado", variable=radio_value, value=2)
      radiobtn1.pack()
      radiobtn2.pack()
      
      btnChangeColor3C = Button(screenRoom3C, text="Escolher", bg="black", fg="white", width=7, height=2, command= exibir3C)
      btnChangeColor3C.pack()
      counter3C +=1
    else:
      messagebox.showinfo("Error","A janela do quarto 3C já está aberta!")

def windowRoom3D():
    global counter3D
    def exibir3D():
      if(radio_value.get() == 1):
        btnBox3D.configure(bg="green")
      elif(radio_value.get() == 2):
        btnBox3D.configure(bg="red")

    if counter3D < 2: 
      screenRoom3D = Toplevel(janela)
      screenRoom3D.title("Quarto 3D")
      screenRoom3D.geometry("400x400")
      
      Label(screenRoom3D,
            text ="This is a new window").pack()
      radio_value=IntVar()
      
      radiobtn1 = Radiobutton(screenRoom3D, text="Vago", variable=radio_value, value=1)
      radiobtn2 = Radiobutton(screenRoom3D, text="Ocupado", variable=radio_value, value=2)
      radiobtn1.pack()
      radiobtn2.pack()
      
      btnChangeColor3D = Button(screenRoom3D, text="Escolher", bg="black", fg="white", width=7, height=2, command= exibir3D)
      btnChangeColor3D.pack()
      counter3D +=1
    else:
      messagebox.showinfo("Error","A janela do quarto 3D já está aberta!")

def windowRoom2A():
    global counter2A
    def exibir2A():
        if(radio_value.get() == 1):
            btnBox2A.configure(bg ="green")
        elif(radio_value.get() == 2):
            btnBox2A.configure(bg ="red")
    
    if counter2A < 2:
        screenRoom2A = Toplevel(janela)
        screenRoom2A.title("Quarto 2A")
        screenRoom2A.geometry("400x400")
        
        Label(screenRoom2A, text = "This is a new window").pack()
        radio_value = IntVar()
        
        radiobtn1 = Radiobutton(screenRoom2A, text="Vago", variable= radio_value, value=1)
        radiobtn2 = Radiobutton(screenRoom2A, text="Ocupado", variable= radio_value, value=2)
        radiobtn1.pack()
        radiobtn2.pack()
        
        btnChangeColor2A = Button(screenRoom2A, text="Escolher", bg="black", fg="white", width=7, height=2, command= exibir2A)
        btnChangeColor2A.pack()
        counter2A +=1
    else:
        messagebox.showinfo("Error", "A janela do quarto 2A já está aberta!")

def windowRoom2B():
    global counter2B
    def exibir2B():
        if(radio_value.get() == 1):
            btnBox2B.configure(bg ="green")
        elif(radio_value.get() == 2):
            btnBox2B.configure(bg ="red")
    
    if counter2B < 2:
        screenRoom2B = Toplevel(janela)
        screenRoom2B.title("Quarto 2B")
        screenRoom2B.geometry("400x400")
        
        Label(screenRoom2B, text = "This is a new window").pack()
        radio_value = IntVar()
        
        radiobtn1 = Radiobutton(screenRoom2B, text="Vago", variable= radio_value, value=1)
        radiobtn2 = Radiobutton(screenRoom2B, text="Ocupado", variable= radio_value, value=2)
        radiobtn1.pack()
        radiobtn2.pack()
        
        btnChangeColor2B = Button(screenRoom2B, text="Escolher", bg="black", fg="white", width=7, height=2, command= exibir2B)
        btnChangeColor2B.pack()
        counter2B +=1
    else:
        messagebox.showinfo("Error", "A janela do quarto 2B já está aberta!")

def windowRoom2C():
    global counter2C
    def exibir2C():
        if(radio_value.get() == 1):
            btnBox2C.configure(bg ="green")
        elif(radio_value.get() == 2):
            btnBox2C.configure(bg ="red")
    
    if counter2C < 2:
        screenRoom2C = Toplevel(janela)
        screenRoom2C.title("Quarto 2C")
        screenRoom2C.geometry("400x400")
        
        Label(screenRoom2C, text = "This is a new window").pack()
        radio_value = IntVar()
        
        radiobtn1 = Radiobutton(screenRoom2C, text="Vago", variable= radio_value, value=1)
        radiobtn2 = Radiobutton(screenRoom2C, text="Ocupado", variable= radio_value, value=2)
        radiobtn1.pack()
        radiobtn2.pack()
        
        btnChangeColor2C = Button(screenRoom2C, text="Escolher", bg="black", fg="white", width=7, height=2, command= exibir2C)
        btnChangeColor2C.pack()
        counter2C +=1
    else:
        messagebox.showinfo("Error", "A janela do quarto 2C já está aberta!")

def windowRoom2D():
    global counter2D
    def exibir2D():
        if(radio_value.get() == 1):
            btnBox2D.configure(bg ="green")
        elif(radio_value.get() == 2):
            btnBox2D.configure(bg ="red")
    
    if counter2D < 2:
        screenRoom2D = Toplevel(janela)
        screenRoom2D.title("Quarto 2D")
        screenRoom2D.geometry("400x400")
        
        Label(screenRoom2D, text = "This is a new window").pack()
        radio_value = IntVar()
        
        radiobtn1 = Radiobutton(screenRoom2D, text="Vago", variable= radio_value, value=1)
        radiobtn2 = Radiobutton(screenRoom2D, text="Ocupado", variable= radio_value, value=2)
        radiobtn1.pack()
        radiobtn2.pack()
        
        btnChangeColor2D = Button(screenRoom2D, text="Escolher", bg="black", fg="white", width=7, height=2, command= exibir2D)
        btnChangeColor2D.pack()
        counter2D +=1
    else:
        messagebox.showinfo("Error", "A janela do quarto 2D já está aberta!")

def windowRoom1A():
    global counter1A
    def exibir1A():
        if(radio_value.get() == 1):
            btnBox1A.configure(bg ="green")
        elif(radio_value.get() == 2):
            btnBox1A.configure(bg ="red")
    
    if counter1A < 2:
        screenRoom1A = Toplevel(janela)
        screenRoom1A.title("Quarto 1A")
        screenRoom1A.geometry("400x400")
        
        Label(screenRoom1A, text = "This is a new window").pack()
        radio_value = IntVar()
        
        radiobtn1 = Radiobutton(screenRoom1A, text="Vago", variable= radio_value, value=1)
        radiobtn2 = Radiobutton(screenRoom1A, text="Ocupado", variable= radio_value, value=2)
        radiobtn1.pack()
        radiobtn2.pack()
        
        btnChangeColor1A = Button(screenRoom1A, text="Escolher", bg="black", fg="white", width=7, height=2, command= exibir1A)
        btnChangeColor1A.pack()
        counter1A +=1
    else:
        messagebox.showinfo("Error", "A janela do quarto 1A já está aberta!")

def windowRoom1B():
    global counter1B
    def exibir1B():
        if(radio_value.get() == 1):
            btnBox1B.configure(bg ="green")
        elif(radio_value.get() == 2):
            btnBox1B.configure(bg ="red")
    
    if counter1B < 2:
        screenRoom1B = Toplevel(janela)
        screenRoom1B.title("Quarto 1B")
        screenRoom1B.geometry("400x400")
        
        Label(screenRoom1B, text = "This is a new window").pack()
        radio_value = IntVar()
        
        radiobtn1 = Radiobutton(screenRoom1B, text="Vago", variable= radio_value, value=1)
        radiobtn2 = Radiobutton(screenRoom1B, text="Ocupado", variable= radio_value, value=2)
        radiobtn1.pack()
        radiobtn2.pack()
        
        btnChangeColor1B = Button(screenRoom1B, text="Escolher", bg="black", fg="white", width=7, height=2, command= exibir1B)
        btnChangeColor1B.pack()
        counter1B +=1
    else:
        messagebox.showinfo("Error", "A janela do quarto 1B já está aberta!")

def windowRoom1C():
    global counter1C
    def exibir1C():
        if(radio_value.get() == 1):
            btnBox1C.configure(bg ="green")
        elif(radio_value.get() == 2):
            btnBox1C.configure(bg ="red")
    
    if counter1C < 2:
        screenRoom1C = Toplevel(janela)
        screenRoom1C.title("Quarto 1C")
        screenRoom1C.geometry("400x400")
        
        Label(screenRoom1C, text = "This is a new window").pack()
        radio_value = IntVar()
        
        radiobtn1 = Radiobutton(screenRoom1C, text="Vago", variable= radio_value, value=1)
        radiobtn2 = Radiobutton(screenRoom1C, text="Ocupado", variable= radio_value, value=2)
        radiobtn1.pack()
        radiobtn2.pack()
        
        btnChangeColor1C = Button(screenRoom1C, text="Escolher", bg="black", fg="white", width=7, height=2, command= exibir1C)
        btnChangeColor1C.pack()
        counter1C +=1
    else:
        messagebox.showinfo("Error", "A janela do quarto 1C já está aberta!")

def windowRoom1D():
    global counter1D
    def exibir1D():
        if(radio_value.get() == 1):
            btnBox1D.configure(bg ="green")
        elif(radio_value.get() == 2):
            btnBox1D.configure(bg ="red")
    
    if counter1D < 2:
        screenRoom1D = Toplevel(janela)
        screenRoom1D.title("Quarto 1D")
        screenRoom1D.geometry("400x400")
        
        Label(screenRoom1D, text = "This is a new window").pack()
        radio_value = IntVar()
        
        radiobtn1 = Radiobutton(screenRoom1D, text="Vago", variable= radio_value, value=1)
        radiobtn2 = Radiobutton(screenRoom1D, text="Ocupado", variable= radio_value, value=2)
        radiobtn1.pack()
        radiobtn2.pack()
        
        btnChangeColor1D = Button(screenRoom1D, text="Escolher", bg="black", fg="white", width=7, height=2, command= exibir1D)
        btnChangeColor1D.pack()
        counter1D +=1
    else:
        messagebox.showinfo("Error", "A janela do quarto 1D já está aberta!")
#Aqui estão todos os botões da tela principal
#Tentaremos colocar a função de criar novos botões de forma mais fácil.
btnBox5A = Button(janela, text="5A", font=("5A", 25), bg="green", fg="white", width=5, height=2, command=windowRoom5A)
btnBox5A.pack()
btnBox5A.place(x=475, y=150)

btnBox5B = Button(janela, text="5B", font=("5B", 25), bg="green", fg="white", width=5, height=2, command=windowRoom5B)
btnBox5B.pack()
btnBox5B.place(x=600, y=150)

btnBox5C = Button(janela, text="5C", font=("5C", 25), bg="green", fg="white", width=5, height=2, command=windowRoom5C)
btnBox5C.pack()
btnBox5C.place(x=725, y=150)

btnBox5D = Button(janela, text="5D", font=("5D", 25), bg="green", fg="white", width=5, height=2, command=windowRoom5D)
btnBox5D.pack()
btnBox5D.place(x=850, y=150)

btnBox4A = Button(janela, text="4A", font=("4A", 25), bg="green", fg="white", width=5, height=2, command=windowRoom4A)
btnBox4A.pack()
btnBox4A.place(x=475, y=275)

btnBox4B = Button(janela, text="4B", font=("4B", 25), bg="green", fg="white", width=5, height=2, command=windowRoom4B)
btnBox4B.pack()
btnBox4B.place(x=600, y=275)

btnBox4C = Button(janela, text="4C", font=("4C", 25), bg="green", fg="white", width=5, height=2, command=windowRoom4C)
btnBox4C.pack()
btnBox4C.place(x=725, y=275)

btnBox4D = Button(janela, text="4D", font=("4D", 25), bg="green", fg="white", width=5, height=2, command=windowRoom4D)
btnBox4D.pack()
btnBox4D.place(x=850, y=275)

btnBox3A = Button(janela, text="3A", font=("3A", 25), bg="green", fg="white", width=5, height=2, command=windowRoom3A)
btnBox3A.pack()
btnBox3A.place(x=475, y=400)

btnBox3B = Button(janela, text="3B", font=("3B", 25), bg="green", fg="white", width=5, height=2, command=windowRoom3B)
btnBox3B.pack()
btnBox3B.place(x=600, y=400)

btnBox3C = Button(janela, text="3C", font=("3C", 25), bg="green", fg="white", width=5, height=2, command=windowRoom3C)
btnBox3C.pack()
btnBox3C.place(x=725, y=400)

btnBox3D = Button(janela, text="3D", font=("3D", 25), bg="green", fg="white", width=5, height=2, command=windowRoom3D)
btnBox3D.pack()
btnBox3D.place(x=850, y=400)

btnBox2A = Button(janela, text="2A", font=("2A", 25), bg="green", fg="white", width=5, height=2, command=windowRoom2A)
btnBox2A.pack()
btnBox2A.place(x=475, y=525)

btnBox2B = Button(janela, text="2B", font=("2B", 25), bg="green", fg="white", width=5, height=2, command=windowRoom2B)
btnBox2B.pack()
btnBox2B.place(x=600, y=525)

btnBox2C = Button(janela, text="2C", font=("2C", 25), bg="green", fg="white", width=5, height=2, command=windowRoom2C)
btnBox2C.pack()
btnBox2C.place(x=725, y=525)

btnBox2D = Button(janela, text="2D", font=("2D", 25), bg="green", fg="white", width=5, height=2, command=windowRoom2D)
btnBox2D.pack()
btnBox2D.place(x=850, y=525)

btnBox1A = Button(janela, text="1A", font=("1A", 25), bg="green", fg="white", width=5, height=2, command=windowRoom1A)
btnBox1A.pack()
btnBox1A.place(x=475, y=650)

btnBox1B = Button(janela, text="1B", font=("1B", 25), bg="green", fg="white", width=5, height=2, command=windowRoom1B)
btnBox1B.pack()
btnBox1B.place(x=600, y=650)

btnBox1C = Button(janela, text="1C", font=("1C", 25), bg="green", fg="white", width=5, height=2, command=windowRoom1C)
btnBox1C.pack()
btnBox1C.place(x=725, y=650)

btnBox1D = Button(janela, text="1D", font=("1D", 25), bg="green", fg="white", width=5, height=2, command=windowRoom1D)
btnBox1D.pack()
btnBox1D.place(x=850, y=650)

janela.mainloop()
=======
from TelaTeste import *

telasDeData.primeiraTela()
>>>>>>> Stashed changes
