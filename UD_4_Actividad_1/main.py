import Utilidades
import gestion_contactos

# tendrá un nombre, un número de teléfono y una dirección de correo electrónico.
contactos = [ ["Ana",67812345,"ana@gmail.com"] ,
              ["Juan",976341234,"juan@gmail.com"]
            ]

def mostrar_menu():
    print("1. Add Contacto")
    print("2. Buscar Contacto")
    print("3. Eliminar Contactos")
    print("4. Mostrar todos")
    print("5. Salir")

while True:
    mostrar_menu()
    opcion = Utilidades.pedir_entero("Dime una opcion")
    match opcion:
        case 1:
            gestion_contactos.add_contacto(contactos)
        case 2:
            gestion_contactos.buscar_contacto(contactos)
        case 3:
            gestion_contactos.eliminar_contacto(contactos)
        case 4:
            gestion_contactos.mostrar_todos(contactos)
        case 5:
            print("Hasta la proxima!!!!")
            # Salimos del bucle
            break
        case _:
            print("Opcion invalida")





