from Funciones import *
class MetodosAbiertos():
    #******* constructor de clase *******#
    def __init__(self) -> None:
        self._error = 0.0
        self._valorInicial = 0
        self._segundoValor = 0
        self._funcion = None
        self._derivadaF = None
        self._iteraciones = 0
        self._raiz = 0.0
        self.MenuInicial()
        
    #******* metodos de instancia *******#
    def MenuInicial(self)->None:
        print("    Metodos abiertos    ")
        print("************************")
        print("Este programa calcula raices")
        print("de funciones utilizando metodos abiertos")
        print("************************")
        self.capturarPolinomio()
        self.elegirMetodo()
    
    def capturarPolinomio(self)->None:
        #impresion de instrucciones
        print("Captura de funcion")
        print("Concidere 0 los faltantes, para construir la funcion")
        print("Ingrese el numero de coeficientes:")
        #captura de grado
        grado = int(input(">>"))-1
        print("************************")
        
        #captura de coeficiemtes
        coeficientes = list()
        for i in range((grado+1)):
            print(f"Ingrese el coeficiente no({i+1})")
            coeficientes.append(float(input(">>")))
        
        #construccion de polinomio
        self._funcion = Polinomio(grado,coeficientes)
        print("Funcion creada!!!!!")
        print("************************")
        
        print("Captura de derivada")
        print("Ingrese el numero de coeficientes:")
        #captura de grado
        gradoD = int(input(">>"))-1
        print("************************")
        
        #captura de coeficiemtes
        coeficientesD = list()
        for i in range((gradoD+1)):
            print(f"Ingrese el coeficiente no({i+1})")
            coeficientesD.append(float(input(">>")))
        
        #construccion de derivada
        self._derivadaF = Polinomio(gradoD,coeficientesD)
        print("Derivada creada!!!!!")
        print("************************")
        
    def elegirMetodo(self)->None:
        #ingresar parametros iniciales
        print("Ingrese el nivel o margen de error:")
        self._error = float(input(">>"))
        print("Error capturado!!!")
        print("*************************")
        
        #imprimir opciones
        print("Eliga el metodo a emplear")
        print("*************************")
        print("1.- Punto fijo")
        print("2.- Newton-Rapson")
        print("3.- Secante")
        opcion = int(input(">>"))
        if opcion == 1:
            print("Ingrese un valor inicial:")
            self._valorInicial = float(input(">>"))
            self.puntoFijo(self._valorInicial, 0)
            self.mostrarResultados()
        elif opcion == 2:
            print("Ingrese un valor inicial:")
            self._valorInicial = float(input(">>"))
            self.NewtonRapson(self._valorInicial, 0)
            self.mostrarResultados()
        elif opcion == 3:
            print("Ingrese un valor inicial:")
            self._valorInicial = float(input(">>"))
            print("ingrese un segundo valor:")
            self._segundoValor = float(input(">>"))
            print("Valores capturados!!!")
            print("*************************")
            self.Secante(self._valorInicial,self._segundoValor,0)
            self.mostrarResultados()
        else:
            print("No hay mas opciones")
    
    def puntoFijo(self, valor, ant)->None:
        Xi = self._funcion.evaluarFuncion(valor)
        error = abs(Xi-ant)/Xi
        
        #condicion de paro
        if error <= self._error:
            #encontro la raiz
            self._raiz = Xi
            self._iteraciones += 1
        else:
            self._iteraciones += 1
            self.puntoFijo(Xi, Xi)
            
    def NewtonRapson(self, valor, ant)->None:
        Xi = valor - (self._funcion.evaluarFuncion(valor))/(self._derivadaF.evaluarFuncion(valor))
        #calculamos el error
        error = abs(Xi-ant)/Xi
        
        #condicion de paro
        if error <= self._error:
            #encontro la raiz
            self._raiz = Xi
            self._iteraciones += 1
        else:
            self._iteraciones += 1
            self.NewtonRapson(Xi, Xi)
    
    def Secante(self, valorS, valorI, ant)->None:
        #calcular Xi
        Xi = valorS - ((self._funcion.evaluarFuncion(valorS))*(valorI-valorS))/(self._funcion.evaluarFuncion(valorI)-self._funcion.evaluarFuncion(valorS))
        #calculamos el error
        error = abs(Xi-ant)/Xi
        
        #condicion de paro
        if error <= self._error:
            #encontro la raiz
            self._raiz = Xi
            self._iteraciones += 1
        else:
            self._iteraciones += 1
            self.Secante(Xi,valorI,Xi)
    
    def mostrarResultados(self)->None:
        print("Resultados")
        print("*************************")
        print(f"funcion dada: {self._funcion}")
        print(f"raiz encontrda: {self._raiz}")
        print(f"iteraciones realizadas: {self._iteraciones}")
    
#******* zona main *******#
if __name__ == "__main__":
    app = MetodosAbiertos()