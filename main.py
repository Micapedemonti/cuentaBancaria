class Persona:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self,nombre,apellido,numero_cuenta,balance):
        super().__init__(nombre,apellido)
        self.numero_cuenta = int(numero_cuenta)
        self.balance = int(balance)


 #Imprimir cliente
    def __str__(self):
        return f"Nombre: {self.nombre} Apellido: {self.apellido} tienes ${self.balance} en tu cuenta numero {self.numero_cuenta},"

    #Funcion retirar dinero
    def retirar(self,cantidad):
        if cantidad > 0 and cantidad <=self.balance:
            self.balance -= cantidad
            print(f"Has retirado: ${cantidad}")
            print(f"Tu saldo actual es de:  ${self.balance}")

        else:
            print("Saldo insuficiente")

 #FUNCION DEPOSITAR
    def depositar (self,cantidad):
        if cantidad > 0 and cantidad:
            self.balance += cantidad
            print(f"Has depositado: $ {cantidad}")
            print(f"Tu saldo actual es de:  ${self.balance}")

        else:
            print("Error, intente mas tarde")

#Funcion crear cliente
def crear_cliente():
    nombre = input("Ingresa tu nombre: ")
    apellido = input("Ingresa tu apellido: ")
    numero_cuenta = input("Ingresa tu número de cuenta: ")
    balance = input("Ingresa el monto inicial en tu cuenta: ")

    return Cliente(nombre, apellido, numero_cuenta, balance)

def inicio():
    cliente = crear_cliente()

    while True:
        print("\nOpciones:")
        print("1. Depositar")
        print("2. Retirar")
        print("3. Ver balance")
        print("4. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            cantidad = int(input("Ingresa la cantidad a depositar: "))
            cliente.depositar(cantidad)
        elif opcion == "2":
            cantidad = int(input("Ingresa la cantidad a retirar: "))
            cliente.retirar(cantidad)
        elif opcion == "3":
            print(cliente)
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

#iniciar programa
inicio()