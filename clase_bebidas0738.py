print("Examen Angel Valencia 0738")
# el constructor funcion
class Bebidas0738:

    def mostrar_datos0738(self):
        print("Angel valencia 0738")
    
    # listas
    def Lista_Bebidas_nombre0738(self):
        mylista0738=["Bacardi","kosako","For loko","Don julio","Gran malo","sky","Caribe"]
        print(mylista0738)
        for nombres0738 in mylista0738:
            print(nombres0738)

    # Tuplas
    def Tupla_Bebidas_Sabor0738(self):
        mitupla0738=("Tamarindo","Mora Azul","Fresa","limon","Citrus","Cereza","Mango")
        print(mitupla0738)
        for sabor0738 in mitupla0738:
            print(sabor0738)

    # Diccionario
    def Diccionario_Bebidas_Precio0738 (self):
        midicc0738 = {
            "Bacardi":"275.00$",
            "kosako":"80.00$",
            "For loko":"300.00$",
            "Don julio":"250.00$",
            "Gran malo":"275.00$",
            "sky":"120.00$",
            "Caribe":"115.00$",
            }
        print(midicc0738)
        for x, y in midicc0738.items():
            print(x, y)

    def altas0738(self):
        print("La operacion se realizo correctamente para los datos de las bebidas")
    def bajas0738(self):
        print("la informacion se guardo correctamente en la base de datos")
# Creacion de objeto info
info=Bebidas0738()

# Utilizando el obj.
info.mostrar_datos0738()
print("")
print(" -lista- ")
print("Lista de nombres de bebidas")
info.altas0738
print("La operacion se realizo correctamente para los datos de las bebidas")
info.bajas0738
print("la informacion se guardo correctamente en la base de datos")
info.Lista_Bebidas_nombre0738()
print("")
print(" -Tupla- ")
print("lista de sabores")
info.altas0738
print("La operacion se realizo correctamente para los datos de las bebidas")
info.bajas0738
print("la informacion se guardo correctamente en la base de datos")
info.Tupla_Bebidas_Sabor0738()
print("")
print(" -Diccionario- ")
print("precio de las bebidas")
info.altas0738
print("La operacion se realizo correctamente para los datos de las bebidas")
info.bajas0738
print("la informacion se guardo correctamente en la base de datos")
info.Diccionario_Bebidas_Precio0738()
print("")
info.altas0738
print("La operacion se realizo correctamente para los datos de las bebidas")
info.bajas0738
print("la informacion se guardo correctamente en la base de datos")
