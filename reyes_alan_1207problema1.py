print("REYES MEZA ALAN EDUARDO_1207 :   3W")  # INFO DE PRACTICA Y PROGRAMADOR 
print(" ")  # ESPACIO

class alumno:
    # clase que representa un alumno con su nombre y su nota
    def __init__(self, nombre, nota):
        # inicializa el objeto alumno con un nombre y una nota
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        # imprime el nombre del alumno, su nota y si esta aprobado o reprobado
        print(f"{self.nombre}: {self.nota} - {'aprobado' if self.nota >= 6 else 'reprobado'}")

class escuela:
    # clase que representa una escuela que contiene una lista de alumnos
    def __init__(self):
        # inicializa la escuela con una lista vacia de alumnos
        self.alumnos = []

    def agregar_alumno(self, nombre, nota):
        # agrega un nuevo alumno a la lista de alumnos
        self.alumnos.append(alumno(nombre, nota))

    def mostrar_aprobados(self):
        # muestra todos los alumnos aprobados (nota >= 6)
        for alumno in self.alumnos:
            if alumno.nota >= 6:
                alumno.imprimir()

    def mostrar_reprobados(self):
        # muestra todos los alumnos reprobados (nota < 6)
        for alumno in self.alumnos:
            if alumno.nota < 6:
                alumno.imprimir()

# ejemplo de uso
escuela = escuela()  # crea una instancia de la clase escuela
escuela.agregar_alumno("alan reyes", 10)  # agrega un alumno con nombre "alan reyes" y nota 10
escuela.agregar_alumno("briana", 5.6)  # agrega un alumno con nombre "briana" y nota 5.6
escuela.agregar_alumno("tito", 9)  # agrega un alumno con nombre "tito" y nota 9

print("aprobados:")
escuela.mostrar_aprobados()  # muestra a los alumnos aprobados

print("\nreprobados:")
escuela.mostrar_reprobados()  # muestra a los alumnos reprobados
