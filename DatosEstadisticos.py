import math
class MainApp():
    #******* metodo constructor *******#
    def __init__(self):
        self._datos = list()
        self._cfs = -2
        self._media = 0
        self._moda = 0
        self._mediana = 0
        self._rango = 0
        self._varianza = 0
        self._desviacion = 0
        self.mainMenu()
    
    #****** Metodos de instancia *******#
    def mainMenu(self):
        print("Sistema estadistico")
        print("*******************")
        print("Eliga la manera de ingresar datos")
        print("1.- Forma manual")
        print("2.- Forma externa (archivo)")
        opcion = int(input(">>"))
        
        if opcion == 1:
            self.capturarDatos()
            self.cicfrasSignificativas()
            self.medidasCentrales()
            self.medidasDispersas()
            self.imprimirResultados()
        elif opcion == 2:
            self.importarDatos()
            self.cicfrasSignificativas()
            self.medidasCentrales()
            self.medidasDispersas()
            self.imprimirResultados()
        else:
            print("no hay mas opciones!!")
            print("*******************")
        
    def capturarDatos(self):
        print("ingrese el numero de datos:")
        print("*******************")
        tamano = int(input(">>"))
        if tamano > 0:
            for i in range(tamano):
                print(f"ingrese dato ({i+1}):")
                self._datos.append(int(input(">>")))
            print("Datos capturados!!!")
        else:
            print("valor invalido")
            
    def importarDatos(self):
        #mensaje de consola
        print("Preparando carga de datos")
        #apertura de archivo
        try:
            #importacion de datos
            with open("..\\Proyectos Python\\MetodosNumericos\\Datos.txt","r") as f:
                linea = f.readline()
                while linea != "":
                    self._datos.append(int(linea))
                    linea = f.readline()
                print("Datos cargados!!!")
                print("****************************")
                f.close()
        except FileNotFoundError as ex:
            print("Error al cargar datos")
            print("****************************")
            
    def cicfrasSignificativas(self):
        print("¿Cuantas cifras desea ver despues del punto decimal? (-1 para omitir)")
        cifras = int(input(">>"))
        if cifras >= 0:
            self._cfs = cifras
            print("cifras configuradas!!!")
            print("****************************")
        else:
            print("Se mostran todos los valores")
            print("****************************")
    
    def medidasCentrales(self):
        #variables temporales
        sumatoria = 0
        muestra = len(self._datos)
        #calculo de media de los datos
        for dato in self._datos:
            sumatoria += dato
        self._media = sumatoria/muestra
        
        #calculo de mediana
        if muestra%2 == 0:
            self._mediana = (self._datos[(muestra//2)-1]+self._datos[(muestra//2)])/2
        else:
            self._mediana = self._datos[(muestra//2)]
        
        #calculo de moda
        self._moda = self.calcularModa()
    
    def calcularModa(self)->int:
        #ordenar datos
        self._datos.sort()
        
        #puntero inicial
        frecuenciaActual = 1
        moda = self._datos[0]
        frecuencia = 1
        
        #barrido de lista
        for i in range(1, len(self._datos)):
            #comprobacion con el valor de atras
            if self._datos[i] == self._datos[i-1]:
                frecuenciaActual += 1
            else:
                frecuenciaActual = 1
                
            #validacion de freciencia relativa e inicial
            if frecuenciaActual > frecuencia:
                moda = self._datos[i]
                frecuencia = frecuenciaActual
        return moda

    def medidasDispersas(self):
        #variables temporales
        sumatoria = 0
        
        #calculo de rango
        self._rango = self._datos[(len(self._datos)-1)] - self._datos[0]
        
        #calculo de varianza
        for dato in self._datos:
            sumatoria += ((dato-self._media)**2)
        self._varianza = sumatoria/(len(self._datos)-1)
        
        #calculo de desviacion estandar
        self._desviacion = math.sqrt(self._varianza)
    
    def reduccion(self, numero, cifras)->float:
        #separar partes
        PE = int(numero)
        PD = numero - PE
        
        #multiplicar
        numeroT = 0
        contador = 1
        contadorCeros = 0
        while True:
            numeroT = PD*(10**contador)
            PET = int(numeroT)
            if PET != 0:
                break
            else:
                contador +=1
                contadorCeros +=1
        
        numero2 = PD*(10**(contadorCeros+cifras))
        #se vuelve a separar
        PE2 = int(numero2)
        PD2 = numero2 - PE2
        
        #truncar/redondear
        if PD2 > 0.5:
            PE2 += 1
        
        #division de parte
        resultado = PE + (PE2/(10**(cifras+contadorCeros)))
        
        #retornamos
        return resultado
        
    def imprimirResultados(self):
        #manipulacion de cifras
        if self._cfs == 0:
            self._media = int(self._media)
            self._varianza = int(self._varianza)
            self._desviacion = int(self._desviacion)
        elif self._cfs > 0:
            self._media = self.reduccion(self._media, self._cfs)
            self._varianza = self.reduccion(self._varianza, self._cfs)
            self._desviacion = self.reduccion(self._desviacion, self._cfs)
            
        print(self.reduccion(0.000437,2))
        
        #impresion de datos
        print("Medidas de tendencia central")
        print("****************************")
        print(f"Media de datos: {self._media}")
        print(f"Mediana de datos: {self._mediana}")
        print(f"Moda de datos: {self._moda}")
        print("****************************")
        
        #impresion de datos
        print("Medidas de dispercion")
        print("****************************")
        print(f"Rango de datos: {self._rango}")
        print(f"Varianza de datos: {self._varianza}")
        print(f"Desviacion de datos: {self._desviacion}")
        print("****************************")
        
        
        
if __name__ == "__main__":
    app = MainApp()