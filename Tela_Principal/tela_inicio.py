import tkinter as tk
from tkinter import *
from tela_data import telasDeData
from tela_checkout import tela_de_checkout

class primeira_tela:
    def tela_primaria(): 
        def proxima_tela():
            tela_inicial.destroy()
            telasDeData.primeiraTela()
            
        tela_inicial = tk.Tk()
        tela_inicial.geometry("300x300")
        tela_inicial.minsize(300, 300)
        tela_inicial.maxsize(300, 300)
        tela_inicial.title("Tela inicial")
        rotuloDoTitulotela_inicial = Label(tela_inicial, bg="dark blue", width=180, height=6)
        rotuloDoTitulotela_inicial.pack()

        ir_checkin = Button(tela_inicial,text="Checkin", bg="dark blue",fg="white", width=8, height=2,command=lambda: proxima_tela())
        ir_checkin.pack()
        ir_checkin.place(x=120,y=150)

        ir_checkout = Button(tela_inicial,text="Checkout", bg="dark blue",fg="white", width=8, height=2,command=lambda: tela_de_checkout.checkout())
        ir_checkout.pack()
        ir_checkout.place(x=120,y=200)
        
        tela_inicial.mainloop()