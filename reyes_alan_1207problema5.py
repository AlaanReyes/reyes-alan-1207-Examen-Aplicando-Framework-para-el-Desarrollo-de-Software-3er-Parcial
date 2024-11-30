print("REYES MEZA ALAN EDUARDO_1207 :   3W")  # INFO DE PRACTICA Y PROGRAMADOR 
print(" ")  # ESPACIO

class Agenda:
    def __init__(self):
        self.contactos = []

    def anadir_contacto(self):
        nombre = input("Nombre: ")
        telefono = input("Telefono: ")
        email = input("Email: ")
        self.contactos.append({"nombre": nombre, "telefono": telefono, "email": email})
        print(f"Contacto {nombre} anadido.")

    def listar_contactos(self):
        if self.contactos:
            for contacto in self.contactos:
                print(f"Nombre: {contacto['nombre']}, Telefono: {contacto['telefono']}, Email: {contacto['email']}")
        else:
            print("No hay contactos.")

    def buscar_contacto(self):
        nombre = input("Nombre a buscar: ")
        for contacto in self.contactos:
            if contacto["nombre"].lower() == nombre.lower():
                print(f"Encontrado: {contacto}")
                return
        print("Contacto no encontrado.")

    def editar_contacto(self):
        nombre = input("Nombre a editar: ")
        for contacto in self.contactos:
            if contacto["nombre"].lower() == nombre.lower():
                contacto["telefono"] = input("Nuevo telefono: ")
                contacto["email"] = input("Nuevo email: ")
                print(f"Contacto {nombre} actualizado.")
                return
        print("Contacto no encontrado.")

    def menu(self):
        while True:
            print("\n1. Anadir contacto\n2. Listar contactos\n3. Buscar contacto\n4. Editar contacto\n5. Cerrar agenda")
            opcion = input("Elige una opcion: ")
            if opcion == "1":
                self.anadir_contacto()
            elif opcion == "2":
                self.listar_contactos()
            elif opcion == "3":
                self.buscar_contacto()
            elif opcion == "4":
                self.editar_contacto()
            elif opcion == "5":
                print("Agenda cerrada.")
                break
            else:
                print("Opcion invalida.")

# Ejecutar el programa
if __name__ == "__main__":
    agenda = Agenda()
    agenda.menu()

