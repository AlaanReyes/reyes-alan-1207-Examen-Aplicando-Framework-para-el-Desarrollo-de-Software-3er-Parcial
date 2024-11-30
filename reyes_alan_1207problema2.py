print("REYES MEZA ALAN EDUARDO_1207 :   3W")  # INFO DE PRACTICA Y PROGRAMADOR 
print(" ")  # ESPACIO

class persona:
    # clase que representa a una persona con su nombre y su edad
    def __init__(self, nombre, edad):
        # inicializa el objeto persona con un nombre y una edad
        self.nombre = nombre
        self.edad = edad

    def mostrar_datos(self):
        # devuelve una cadena con el nombre y la edad de la persona
        return f"{self.nombre}, {self.edad} años"

    def es_mayor_de_edad(self):
        # determina si la persona es mayor de edad (edad >= 18)
        return "mayor de edad" if self.edad >= 18 else "menor de edad"

    def grupo_de_edad(self):
        # clasifica a la persona según su edad en un grupo de edad
        if self.edad < 13: return "niño"
        if self.edad < 18: return "adolescente"
        if self.edad < 60: return "adulto"
        return "adulto mayor"

# ejemplo de uso
persona1 = persona("alan reyes", 19)  # crea una persona con nombre "alan reyes" y edad 19
persona2 = persona("briana", 15)  # crea una persona con nombre "briana" y edad 15
persona3 = persona("tito", 61)  # crea una persona con nombre "tito" y edad 61

# muestra los datos de cada persona, si es mayor de edad y su grupo de edad
print(persona1.mostrar_datos(), "-", persona1.es_mayor_de_edad(), "-", persona1.grupo_de_edad())
print(persona2.mostrar_datos(), "-", persona2.es_mayor_de_edad(), "-", persona2.grupo_de_edad())
print(persona3.mostrar_datos(), "-", persona3.es_mayor_de_edad(), "-", persona3.grupo_de_edad())

