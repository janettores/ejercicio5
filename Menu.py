#from ClasePlanAhorro import PlanAhorro
class Menu:
    __opcion = None
    __lista = None

    def __init__(self, opcion, lista):
        self.__opcion = opcion
        self.__lista = lista

    def ActualizarValor(self):
        for i in range(len(self.__lista)):
            print("Cod: {}, Modelo: {}, Version: {}".format(self.__lista[i].getCod(), self.__lista[i].getModelo(), self.__getVersion()))
            self.__lista[i].modificarValor(int(input("Ingrese el valor del Vehiculo: \n")))

    def MenuOp(self):
        if self.__opcion == 1:
            self.ActualizarValor()