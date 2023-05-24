from tkinter import *
import tkinter as tk
from database import *
database = RoomDB()

class TelaDeResumo:
    def quartaTela():
        telaQuatro = tk.Tk()
        telaQuatro.geometry("300x300")
        telaQuatro.minsize(300, 300)
        telaQuatro.maxsize(300, 300)
        telaQuatro.title("Resumo")
    

        