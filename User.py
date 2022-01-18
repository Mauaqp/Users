class User:
    def __init__(self,name = "N/A", surname = "N/A",balance = 0,):
        self.name = name
        self.surname = surname
        self.balance = balance
    
    def hacer_retiro(self, amount):
        self.nuevoBalance = self.balance - amount
        self.balance = self.nuevoBalance
        print("El nuevo balance es: " + str(self.balance))

    def hacer_deposito(self, amount):
        self.nuevoBalance = self.balance + amount
        self.balance = self.nuevoBalance
        print("El nuevo balance es: " + str(self.balance))
    
    def transferencia(self,other_user,amount):
        self.nuevoBalance = self.balance - amount
        self.balance = self.nuevoBalance
        other_user.nuevoBalance = other_user.balance + amount
        other_user.balance = other_user.nuevoBalance
        print("---- Transferencia ----")
        print(self.name + " ha transferido " + str(amount) + " a " + other_user.name)
        print(other_user.name +" - " + str(other_user.balance))
        print(self.name +" - " + str(self.balance))
        

    def imprimeInfo ( self):
        print("----------")
        print(self.name + " " + self.surname + " " +str(self.balance)+" Soles")