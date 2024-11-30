print("REYES MEZA ALAN EDUARDO_1207 :   3W")  # INFO DE PRACTICA Y PROGRAMADOR 
print(" ")  # ESPACIO

class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        """Inicializa los tres lados del triangulo"""
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def lado_mayor(self):
        """Devuelve el valor del lado con mayor tamano"""
        return max(self.lado1, self.lado2, self.lado3)

    def tipo_triangulo(self):
        """Determina el tipo de triangulo"""
        if self.lado1 == self.lado2 == self.lado3:
            return "Equilatero"
        elif self.lado1 == self.lado2 or self.lado2 == self.lado3 or self.lado1 == self.lado3:
            return "Isosceles"
        else:
            return "Escaleno"

def ingresar_datos():
    """Funcion para ingresar los datos del triangulo desde el teclado"""
    try:
        lado1 = float(input("Introduce el primer lado del triangulo: "))
        lado2 = float(input("Introduce el segundo lado del triangulo: "))
        lado3 = float(input("Introduce el tercer lado del triangulo: "))

        # Crear el objeto Triangulo
        triangulo = Triangulo(lado1, lado2, lado3)

        # Mostrar el lado mayor y el tipo de triangulo
        print(f"\nLado mayor del triangulo: {triangulo.lado_mayor()}")
        print(f"Tipo de triangulo: {triangulo.tipo_triangulo()}")

    except ValueError:
        print("Por favor, introduce un valor numerico valido.")

# Ejecutar el programa
if __name__ == "__main__":
    ingresar_datos()
