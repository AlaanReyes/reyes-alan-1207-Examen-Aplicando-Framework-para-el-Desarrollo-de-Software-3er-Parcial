print("REYES MEZA ALAN EDUARDO_1207 :   3W")  # INFO DE PRACTICA Y PROGRAMADOR 
print(" ")  # ESPACIO

class Calculadora:
    def __init__(self, num1, num2):
        """Inicializa los dos numeros enteros"""
        self.num1 = num1
        self.num2 = num2

    def suma(self):
        """Realiza la suma de los dos numeros"""
        return self.num1 + self.num2

    def resta(self):
        """Realiza la resta de los dos numeros"""
        return self.num1 - self.num2

    def multiplicacion(self):
        """Realiza la multiplicacion de los dos numeros"""
        return self.num1 * self.num2

    def division(self):
        """Realiza la division de los dos numeros. Maneja division por cero"""
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Error: No se puede dividir por cero."

# Funcion para ingresar los datos y realizar las operaciones
def ingresar_datos():
    try:
        # Pedir los numeros al usuario
        num1 = int(input("Introduce el primer numero entero: "))
        num2 = int(input("Introduce el segundo numero entero: "))

        # Crear el objeto Calculadora
        calc = Calculadora(num1, num2)

        # Imprimir los resultados de las operaciones
        print(f"\nSuma: {calc.suma()}")
        print(f"Resta: {calc.resta()}")
        print(f"Multiplicacion: {calc.multiplicacion()}")
        print(f"Division: {calc.division()}")
    
    except ValueError:
        print("Por favor, ingresa solo numeros enteros validos.")

# Ejecutar el programa
if __name__ == "__main__":
    ingresar_datos()
