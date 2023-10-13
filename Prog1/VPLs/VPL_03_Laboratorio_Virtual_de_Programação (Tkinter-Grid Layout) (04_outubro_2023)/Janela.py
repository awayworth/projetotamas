from tkinter import *

class Janela( Tk ):
    __Lb_nome = None
    __Lb_telefone = None
    __Lb_email = None
    __Lb_endereco = None
    __Et_nome = None
    __Et_telefone = None
    __Et_email = None
    __Et_endereco = None
    
    def __init__(self, Str="Janela"):
        super().__init__()
        super().title(Str)
        super().geometry("%dx%d+%d+%d"% (420,95,400,150))
        super().configure(bg="orange")
        
        self.inicialize()
    
    def inicialize(self):

        self.__Lb_nome=Label(self, text="Nome:", width=15)
        self.__Lb_telefone=Label(self, text="Telefone:", width=15)
        self.__Lb_email=Label(self, text="Email:", width=15)
        self.__Lb_endereco=Label(self, text="Endereço:", width=15)
    
        self.__Lb_nome.configure(bg='yellow', anchor="e")
        self.__Lb_telefone.configure(bg='yellow', anchor="e")
        self.__Lb_email.configure(bg='yellow', anchor="e")
        self.__Lb_endereco.configure(bg='yellow', anchor="e") 
    
        self.__Et_nome=Entry(self, width=42)
        self.__Et_telefone=Entry(self, width=42)
        self.__Et_email=Entry(self, width=42)
        self.__Et_endereco=Entry(self, width=42)
        
        self.__Lb_nome.grid(row=0, column=0, padx=2, pady=2)
        self.__Lb_telefone.grid(row=1, column=0, padx=2, pady=2)
        self.__Lb_email.grid(row=2, column=0, padx=2, pady=2)
        self.__Lb_endereco.grid(row=3, column=0, padx=2, pady=2)
        self.__Et_nome.grid(row=0, column=1, padx=2, pady=2)
        self.__Et_telefone.grid(row=1, column=1, padx=2, pady=2)
        self.__Et_email.grid(row=2, column=1, padx=2, pady=2)
        self.__Et_endereco.grid(row=3, column=1, padx=2, pady=2)

