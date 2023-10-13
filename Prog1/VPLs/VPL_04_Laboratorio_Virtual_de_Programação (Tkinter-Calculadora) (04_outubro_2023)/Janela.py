from tkinter import *

class Janela( Tk ):
    __Lb_valor1=None
    __Lb_valor2=None
    __Lb_result=None
    __Et_valor1=None
    __Et_valor2=None
    __Et_result=None
    __Bt_adic=None
    __Bt_sub=None
    __Bt_mult=None
    __Bt_div=None
    
    def __init__(self, Str="Janela"):
        super().__init__()
        super().title(Str)
        super().geometry("%dx%d+%d+%d"%(380,140,100,100))
        super().configure(bg="orange")
        
        self.inicialize()
    
    def action_exit(self):

        print("Destruindo a Janela...")
        self.destroy()
        sys.exit(0)
        
    def action_Bt_adic(self):

        n1 = float(self.__Et_valor1.get())
        n2 = float(self.__Et_valor2.get())
        total = n1 + n2
        self.__Et_result.delete(0, END)
        self.__Et_result.insert(END, "%5.2f"%total)
        
    def action_Bt_sub(self):

        n1 = float(self.__Et_valor1.get())
        n2 = float(self.__Et_valor2.get())
        total = n1 - n2
        self.__Et_result.delete(0, END)
        self.__Et_result.insert(END, "%5.2f"%total)
        
    def action_Bt_mult(self):

        n1 = float(self.__Et_valor1.get())
        n2 = float(self.__Et_valor2.get())
        total = n1 * n2
        self.__Et_result.delete(0, END)
        self.__Et_result.insert(END, "%5.2f"%total)
        
    def action_Bt_div(self):

        n1 = float(self.__Et_valor1.get())
        n2 = float(self.__Et_valor2.get())
        total = n1 / n2
        self.__Et_result.delete(0, END)
        self.__Et_result.insert(END, "%5.2f"%total)
        
    def inicialize(self):

        self.__Lb_valor1=Label(self,text="Valor1:",width=12)
        self.__Lb_valor2=Label(self,text="Valor2:",width=12)
        self.__Lb_result=Label(self,text="Resultado:",width=12)
        
        self.__Lb_valor1.configure(bg="yellow", anchor=E)
        self.__Lb_valor2.configure(bg="yellow", anchor=E)
        self.__Lb_result.configure(bg="yellow", anchor=E)
        
        self.__Et_valor1=Entry(self,width="28")
        self.__Et_valor2=Entry(self,width="28")
        
        self.__Et_result = Entry(self, widt="28")
        self.__Et_result.configure(bg="lightgray")
        
        self.__Bt_adic=Button(self, text='Adic', command=self.action_Bt_adic)

        self.__Bt_sub=Button(self, text='Sub', command=self.action_Bt_sub)

        self.__Bt_mult=Button(self, text='Mult', command=self.action_Bt_mult)

        self.__Bt_div=Button(self, text='Div', command=self.action_Bt_div)

        self.__Lb_valor1.grid(row=0, column=0, sticky=NW, padx=4, pady=4)
        self.__Lb_valor2.grid(row=1, column=0, sticky=NW, padx=4, pady=4)
        
        self.__Lb_result.grid(row=3, column=0, sticky=NW, padx=4, pady=4)
        self.__Et_result.grid(row=3, column=1, columnspan=4, sticky=NW, padx=4, pady=4)
        
        self.__Et_valor1.grid(row=0, column=1, columnspan=4, sticky=NW, padx=4, pady=4)
        self.__Et_valor2.grid(row=1, column=1, columnspan=4, sticky=NW, padx=4, pady=4)
        
        self.__Bt_adic.grid(row=2, column=1, sticky=NW, padx=4, pady=4)
        self.__Bt_sub.grid(row=2, column=2, sticky=NW, padx=4, pady=4)
        self.__Bt_mult.grid(row=2, column=3, sticky=NW, padx=4, pady=4)
        self.__Bt_div.grid(row=2, column=4, sticky=NW, padx=4, pady=4)
        
        self.protocol("WM_DELETE_WINDOW", self.action_exit)

