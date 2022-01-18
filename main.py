from User import User

alberto = User("Alberto", "Durer", 1000)
ernesto = User("Ernesto", "Valencia", 15000)
pedro = User ("Pedro", "Peraltilla", 300000)
paula = User("Paula", "Rodriguez", 50)


paula.imprimeInfo()
paula.hacer_retiro(10)
paula.imprimeInfo()

#Haz que el primer usuario haga 3 depósitos y 1 giro, y luego muestra sus balances

alberto.hacer_deposito(200) # Depósito 1
alberto.imprimeInfo()
alberto.hacer_deposito(500) #Depósito 2
alberto.imprimeInfo()
alberto.hacer_deposito(5) #Depósito 3
alberto.imprimeInfo()

# Haz que el segundo usuario haga 2 depósitos y 2 giros, y luego muestra sus balances
ernesto.imprimeInfo()
ernesto.hacer_deposito(150)# Depósito 1
ernesto.hacer_deposito(745)# Depósito 2
ernesto.hacer_retiro(1000) # Giro 1
ernesto.hacer_retiro(1450) # Giro 2
ernesto.imprimeInfo()

#Haz que el tercer usuario haga 1 depósito y 3 giros, y luego muestra sus balances
pedro.imprimeInfo()
pedro.hacer_deposito(100) #Depósito 1
pedro.hacer_retiro(13) # Giro 1
pedro.hacer_retiro(5) # Giro 2
pedro.hacer_retiro(200) # Giro 3
pedro.imprimeInfo()

#BONUS: Agrega un método transferir_dinero; 
# haz que el primer usuario transfiera dinero al tercer usuario y luego imprime los balances de ambos usuarios

ernesto.transferencia(paula, 12000)

