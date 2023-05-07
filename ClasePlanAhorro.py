class PlanAhorro:
    __cod = None
    __modelo = ''
    __versionVeh = ''
    __precio = 0.0
    __cantCuotas = None  # variable de clase
    __cantCuotasLicita = None  # Variable de clase

    def __init__(self, cod, modelo, versionVeh, precio):
        self.__cod = cod
        self.__modelo = modelo
        self.__versionVeh = versionVeh
        self.__precio = precio

    @classmethod
    def ModificarPlan(cls, valor):
        cls.__cantCuotas = valor

    @classmethod
    def ModicarLic(cls, valor):
        cls.__cantCuotasLicita = valor

    def modificarValor(self, valor):
        self.__precio = valor

    def getCod(self):
        return self.__cod

    def getModelo(self):
        return self.__modelo

    def getVersion(self):
        return self.__versionVeh

    def getPrecio(self):
        return self.__precio