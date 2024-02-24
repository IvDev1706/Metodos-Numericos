
class Bisectriz():
    #******* Metodo constructor *******#
    def __init__(self) -> None:
        self._coeficientes = list()
        self._intervalo = tuple()
        self._error = 0.0
        self._raiz = 0.0
        self._grado = 0
        self._existe = True
        self.menuPrincipal()
        a, b = self._intervalo
        self.bisectriz(a, b)
        self.ImprimirResultados()
    #******* Metodos de instancia *******#
    def menuPrincipal(self)->None:
        print("Metodo de la bisectriz")
        print("**********************")
        print("Encuentre las raices de su polinomio rapidamente")
        print("Mediante el uso del metodo de la bisectriz en funciones")
        print("**********************")
        
        #captura del numero de coeficientes
        print("concidere 0 los coeficientes faltantes,")
        print("el orden de ingreso sera del grado mayor al menor")
        print("Ingrese la cantidad de coeficientes: ")
        coeficientes = int(input(">> "))
        print("Numero capturado!!")
        print("**********************")
        
        #configuracion de grado y captura de coeficientes
        self._grado = coeficientes-1
        for i in range(coeficientes):
            print(f"Ingrese coeficiente no({i+1})")
            self._coeficientes.append(int(input(">> ")))
        print("Coeficientes capturados!!")
        print("**********************")
        
        #captura de intervalo estimado
        print("Ingrese el intervalo estimado: ")
        a = int(input("(a) >> "))
        b = int(input("(b) >> "))
        self._intervalo = (a,b)
        print("Intervalo capturado!!")
        print("**********************")
        
        #captura del error permitido
        print("Ingrese el error/tolerancia permitido: ")
        self._error = float(input(">> "))
        print("Error capturado!!")
        print("**********************")
        
     #metodo para encontrar una raiz mediante el metodo de la bisectriz   
    def bisectriz(self, a, b)->None:
        #condicion de paro
        if a < b:
            #calcular punto medio
            puntoMedio = (b+a)/2
            
            #evaluaciones en la funcion
            fMedia = self.evaluarFuncion(puntoMedio)
            fInferior = self.evaluarFuncion(a)
            
            #validaciones de raices
            if fMedia == 0:
                self._raiz = puntoMedio
            else:
                #obtener producto de funciones
                producto = fMedia*fInferior
                #tres casos posibles
                if producto == 0:
                    self._raiz = puntoMedio
                elif producto < 0:
                    self.bisectriz(a,puntoMedio)
                elif producto > 0:
                    self.bisectriz(puntoMedio,b)
        else:
            self._existe = False
                
    #metodo recursivo para evaluar la funcion delvalor dado
    def evaluarFuncion(self, valor)->float:
        resultado = 0
        exp = self._grado
        for coef in self._coeficientes:
            resultado += coef*(valor**exp)
            exp -= 1
        return resultado
    
    def ImprimirResultados(self)->None:
        print("Resultados")
        print("*************************")
        print("polinomio dado: ")
        for coeficiente in self._coeficientes:
            if self._grado > 0:
                print(f"{coeficiente}x^{self._grado}", end=" + ")
                self._grado -= 1
            else:
                print(f"{coeficiente}")
        a, b = self._intervalo
        print(f"intervalo dado [{a},{b}]")
        print(f"¿existe raiz?: {self._existe}")
        if self._existe:
            print(f"Raiz encontrada en X = ({self._raiz})")
        else:
            print("intente con otro intervalo")
        print("*************************")

if __name__ == "__main__":
    app = Bisectriz()