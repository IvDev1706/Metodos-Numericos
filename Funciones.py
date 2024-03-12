import math
class Polinomio():
    def __init__(self, grado, coef) -> None:
        self._grado = grado
        self._coeficientes = coef
    
    def evaluarFuncion(self, valor)->float:
        resultado = 0
        exp = self._grado
        for coef in self._coeficientes:
            resultado += coef*(valor**exp)
            exp -= 1
        return resultado
            
    def __str__(self) -> str:
        salida = ""
        exp = self._grado
        for coeficiente in self._coeficientes:
            if exp > 0:
                if coeficiente!=0:
                    salida += f"{coeficiente}x^{exp}"+" + "
                exp -= 1
            else:
                salida += f"{coeficiente}"
        return salida
