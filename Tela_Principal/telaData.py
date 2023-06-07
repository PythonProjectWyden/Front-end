# import tkinter as tk
# import telaQuartos
# from tkinter import *
# from database import *
# from tkcalendar import DateEntry
# from datetime import datetime 
# database = RoomDB()

<<<<<<< Updated upstream
# class telasDeData:
#     checkinDentro = None
#     checkoutDentro = None
=======
class telasDeData:
    def primeiraTela(): 
        def saveDates():
            with open('dates.txt', 'a') as f:
                checkin1 = checkin_date.get_date()
                checkout1 = checkout_date.get_date()
                f.write("{}:{}".format(checkin1,checkout1))
                f.close()
                if(checkin1 > checkout1):
                    return
                else:
                    telaUm.destroy()
                    database.insert_room(NONE,NONE,NONE,NONE,NONE,0)
                    telaQuartos.telasDeQuartos.segundaTela()
                
        telaUm = tk.Tk()
        telaUm.eval('tk::PlaceWindow . center')
        telaUm.geometry("300x300")
        telaUm.minsize(300, 300)
        telaUm.maxsize(300, 300)
        telaUm.title("Check-In e Check-Out")
        rotuloDoTituloTelaUm = Label(telaUm, bg="dark blue", width=180, height=6)
        rotuloDoTituloTelaUm.pack()
>>>>>>> Stashed changes

#     def proxTelas():
#         telaQuartos.telasDeQuartos.segundaTela()
  
#     def primeiraTela():




#         telaUm = tk.Tk()
#         telaUm.geometry("300x300")
#         telaUm.minsize(300, 300)
#         telaUm.maxsize(300, 300)
#         telaUm.title("Check-In e Check-Out")
#         rotuloDoTituloTelaUm = Label(telaUm, bg="dark blue", width=180, height=6)
#         rotuloDoTituloTelaUm.pack()

#         tituloTelaUm1 = Label(telaUm, text="Wyden Hotel", font=("Wyden Hotel", 20), bg="dark blue", fg="white",)
#         tituloTelaUm1.pack()
#         tituloTelaUm1.place(x=70, y=30)

#         tituloTelaUm2 = Label(telaUm, text="Datas:", font=("Datas", 18))
#         tituloTelaUm2.pack()

#         LabelTelaUm1 = tk.Label(telaUm, text="Data Check-in:")
#         LabelTelaUm1.pack()
#         LabelTelaUm1.place(x=100,y=130)

#         checkin_date = DateEntry(telaUm, width=12, background='darkblue', foreground='white', borderwidth=2, mindate = datetime(2023,1,1),
#                                   maxdate = datetime(2023,12,31), showweeknumbers = False, showothermonthdays = False)
#         checkin_date.pack(padx=10, pady=10)
#         checkin_date.place(x=100,y=150)

#         LabelTelaUm2 = tk.Label(telaUm, text="Data Check-out:")
#         LabelTelaUm2.pack()
#         LabelTelaUm2.place(x=100,y=180)

#         checkout_date = DateEntry(telaUm, width=12, background='darkblue', foreground='white', borderwidth=2, mindate = datetime(2023,1,1),
#                                    maxdate = datetime(2023,12,31), showweeknumbers = False, showothermonthdays = False)
#         checkout_date.pack(padx=10, pady=10)
#         checkout_date.place(x=100,y=200)

#         continuar = Button(telaUm,text="Salvar Datas", bg="dark blue",fg="white", width=8, height=2,command=lambda: (telasDeData.proxTelas(),
#                                                                                                                      telaUm.destroy()))
#         continuar.pack()
#         continuar.place(x=120,y=250)

#         telaUm.mainloop()

#         login = checkout_date
#         with open("password.txt","a") as arquivo:
#             arquivo.write(login)
#             print('Usuario cadastrado com sucesso!')

#         # def autenticar_user():
#         #     with open("password.txt","r") as arquivo:
#         #         for linha in arquivo:
#         #             linha = linha.strip()
#         #             usuario, senha_salva = linha.split(":")

#         #         if usuario == login and senha == senha_salva:
#         #             return True
#         #         return False