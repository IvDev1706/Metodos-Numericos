#******* Variables globales *******#
total = 0
tacos = 0
tortas = 0
quesadillas = 0
cocas = 0
pepsis = 0
papas = False
chiles = False

#******* Metodos *******#
def menuPlatos():
    global total, tacos, tortas, quesadillas
    continuar = True
    while continuar:
        #impresion de menu
        print("    Taqueria MN    ")
        print("*******************")
        print("¿Que desea ordenar?")
        print("1.- Tacos")
        print("2.- Tortas")
        print("3.- Quesadillas")
        print("*******************")
        #captura de opcion
        opcion = int(input(">>"))
        #evaluacion de opcion
        if opcion == 1:
            print("¿Cuantos va a querer?")
            tacos = int(input(">>"))
            total += tacos*10
            print("¿Desea algo mas?(s/n)")
            decision = input(">>")
            if decision == "n":
                continuar = False
        elif opcion == 2:
            print("¿Cuantas va a querer?")
            tortas = int(input(">>"))
            total += tortas*20
            print("¿Desea algo mas?(s/n)")
            decision = input(">>")
            if decision == "n":
                continuar = False
        elif opcion == 3:
            print("¿Cuantas va a querer?")
            quesadillas = int(input(">>"))
            total += quesadillas*25
            print("¿Desea algo mas?(s/n)")
            decision = input(">>")
            if decision == "n":
                continuar = False
        else:
            print("No hay mas opciones")

def menuAcompanante():
    global papas, chiles, total
    #impresion de menu
    print("     Taqueria MN    ")
    print("********************")
    print("¿Con que desea acompañar?")
    print("1.- Papas")
    print("2.- Chiles")
    print("3.- Nada")
    print("********************")
    #captura de opcion
    opcion = int(input(">>"))
    #evaluacion de opcion
    if opcion == 1:
        print("Papas agregadas")
        total += 8
    elif opcion == 2:
        print("Chiles agregados")
        total += 10
    elif opcion == 3:
        print("Sin acompañantes")
    else:
        print("No hay mas opciones")
       
def menuBebidas():
    global total, cocas, pepsis
    continuar = True
    while continuar:
        #impresion de menu
        print("    Taqueria MN    ")
        print("*******************")
        print("¿Que bebida(s) desea?")
        print("1.- Coca")
        print("2.- Pepsi")
        print("*******************")
        #captura de opcion
        opcion = int(input(">>"))
        #evaluacion de opcion
        if opcion == 1:
            print("¿Cuantas va a querer?")
            cocas = int(input(">>"))
            total += cocas*17
            print("¿Desea algo mas?(s/n)")
            decision = input(">>")
            if decision == "n":
                continuar = False
        elif opcion == 2:
            print("¿Cuantas va a querer?")
            pepsis = int(input(">>"))
            total += pepsis*16
            print("¿Desea algo mas?(s/n)")
            decision = input(">>")
            if decision == "n":
                continuar = False
        else:
            print("No hay mas opciones")

def imprimirComporbante():
    global total, tacos, tortas, quesadillas, chiles, papas, cocas, pepsis
    #impresion de orden y precios
    print("      Ticket de orden      ")
    print("***************************")
    print(f"Tacos: {tacos} costo: {tacos*10}")
    print(f"Tortas: {tortas} costo: {tortas*20}")
    print(f"Tacos: {quesadillas} costo: {quesadillas*25}")
    print("***************************")
    if papas:
        print("Acompañante: papas costo: 8")
    elif chiles:
        print("Acompañante: chiles costo: 10")
    else:
        print("Sin acompañantes costo: 0")
    print("***************************")
    print(f"Cocas: {cocas} costo: {cocas*17}")
    print(f"Pepsis: {pepsis} costo: {pepsis*16}")
    print("***************************")
    print(f"total a pagar: {total}")
    

#******* Zona main *******#
if __name__ == "__main__":
    menuPlatos()
    menuAcompanante()
    menuBebidas()
    imprimirComporbante()