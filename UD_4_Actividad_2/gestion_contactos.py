import email

import Utilidades

def add_contacto(contactos):
    nombre = Utilidades.pedir_texto("Ingrese el nombre del contacto: ")
    telefono = Utilidades.pedir_entero("Ingrese el telefono del contacto: ")
    email = Utilidades.pedir_texto("Ingrese el email del contacto: ")
    if email in contactos:
        print("El contacto ya existe")
    else:
        contactos[email] = {"telefono" : telefono, "nombre" : nombre}


def buscar_contacto(contactos):
    email = Utilidades.pedir_texto("Ingrese el email del contacto: ")
    if email in contactos:
        print(f"{'Nombre':<20} {'Telefono':<15} {'Email':<20}")
        print("-" * 55)
        print(f"{contactos[email]['nombre']:<20} {contactos[email]['telefono']:<15} {email:<20}")
    else:
        print("Contacto no encontrado")

def eliminar_contacto(contactos):
    email = Utilidades.pedir_texto("Ingrese el email del contacto: ")
    if email in contactos:
        contactos.pop(email)
        print("Contacto eliminado")
    else:
        print("Contacto no existe")

def mostrar_todos(contactos):
    if len(contactos) == 0:
        print("No hay contactos")
    else:
        print(f"{'Nombre':<20} {'Telefono':<15} {'Email':<20}")
        print("-"*55)
        for email, valor in contactos.items():
            print(f"{valor['nombre']:<20} {valor['telefono']:<15} {email:<20}")


Persona p = new Persona()

Persona p1 = p

p1.setNombre("juan")