import csv

class Vehiculo ():
    def __init__(self, marca, modelo, nro_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.nro_ruedas = nro_ruedas
        

    def guardar_datos_csv (self):
        try:
            with open ("vehiculos.csv", "a", newline ="") as archivo:
                datos = [(self.__class__, self.__dict__)]
                archivo_csv = csv.writer (archivo)
                archivo_csv.writerows(datos)
        except FileNotFoundError:
            print ("No existe el archivo vehiculos.csv")
        except Exception as e:
            print ("Error reportado", e)

    
    def leer_datos_csv (self):
        try:
            with open ("vehiculos.csv", "r") as archivo:
                vehiculos = csv.reader (archivo)
                print (f"Lista de Vehiculos{type(self).__name__}")
                for item in vehiculos:
                    vehiculo_tipo = str(self.__class__)
                    if vehiculo_tipo in item [0]:
                        print (item[1])
                print ("")
        except FileNotFoundError:
            print ("No existe el archivo vehiculos.csv")
        except Exception as e:
            print ("Error reportado", e)


    
    def __str__(self):
        return f"Marca {self.marca}, modelo {self.modelo}, {self.nro_ruedas} ruedas"
    


class Automovil(Vehiculo):
    def __init__ (self, marca, modelo, nro_ruedas, velocidad, cilindraje):
        super().__init__(marca, modelo, nro_ruedas)
        self.velocidad = velocidad
        self.cilindraje = cilindraje

    def __str__(self):
        return super().__str__() + f"{self.velocidad}, {self.cilindraje} cc"
    


class Particular (Automovil):
    def __init__ (self, marca, modelo, nro_ruedas, velocidad, cilindraje, npuesto):
        super().__init__ (marca, modelo, nro_ruedas, velocidad, cilindraje)
        self.npuesto = npuesto

    def get_npuesto(self):
        return self.npuesto
    
    def set_npuesto(self, npuesto_new ): 
        self.npuesto = npuesto_new

    def __str__(self):
        return super().__str__() + f", puestos: {self.npuesto}"
    

class Carga (Automovil):
    def __init__ (self, marca, modelo, nro_ruedas, velocidad, cilindraje, pesodecarga):
        super().__init__(marca, modelo, nro_ruedas, velocidad, cilindraje)
        self.pesodecarga = pesodecarga

    def __str__(self):
        return super().__str__() + f", peso de carga: {self.pesodecarga}"
    
class Bicicleta (Vehiculo):
    def __init__(self, marca, modelo, nro_ruedas, tipo):
        super().__init__(marca, modelo, nro_ruedas)
        self.tipo = tipo

    def __str__(self):
        return super().__str__() + f", tipo de bicicleta: {self.tipo}"
    
class Motocicleta (Bicicleta):
    def __init__(self, marca, modelo, nro_ruedas, tipo, nradios, cuadro, motor):
        super().__init__(marca, modelo, nro_ruedas, tipo)
        self.nradios = nradios
        self.cuadro = cuadro
        self.motor = motor

    def __str__(self):
        return super().__str__() + f", {self.nradios} radios, cuadro: {self.cuadro}, motor: {self.motor}"