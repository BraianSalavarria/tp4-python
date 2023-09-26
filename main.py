#Para el correcto funcionamiento de cada uno de los ejercicios, por favor descomentar el ejercicio a testear y comentar los demas.
import os

def borrarPantalla(): #Funcion que nos permitira borrar la consola
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "dos" or os.name == "nt":
        os.system ("cls")

"""
Ejercicio 1: 
    Realizar un programa que pida al usuario un número entero del 0 al 9, y que mientras el número no 
sea correcto se repita el proceso. Luego debe comprobar si el número se encuentra en la lista de 
números y notificarlo:


lista_numeros = [0,1,2,3,4,5,6,7,8,9]
numero_correcto = False

while numero_correcto != True:
    numero_ingresado = int(input('Ingrese un numero entre 0 y 9: '))
    if numero_ingresado in lista_numeros:
        print('El numero ingresado es correcto !!!')
        numero_correcto = True
    else:
        print('El numero ingresado es incorrecto !!!')

"""
# ********************************************************

"""
Ejercicio 2: 
   Realiza un programa que siga las siguientes instrucciones:
• Crea un conjunto llamado usuarios con los usuarios Marcela, David, Elvira, Juan y Marcos
• Crea un conjunto llamado administradores con los administradores Juan y Marcela.
• Borra al administrador Juan del conjunto de administradores.
• Añade a Marcos como un nuevo administrador, pero no lo borres del conjunto de usuarios.
• Muestra todos los usuarios por pantalla de forma dinámica, además debes indicar cada 
usuario es administrador o no.
 
 
usuarios = {'Marcela', 'David', 'Elvira', 'Juan', 'Marcos'}
administradores = {'Juan', 'Marcela'}

print(administradores)

#Eliminamos al administrador juan
administradores.discard('Juan')

print(administradores)

administradores.add('Marcos')

print(administradores)

for usuario in usuarios:
    if usuario in administradores:
        print('Usuario: ' + usuario + ". Es administrador.")
    else:
        print('Usuario: ' + usuario + ". No es administrador.")
        
"""
# ********************************************************

"""
Ejercicio 3: 
   Realiza una función separar(lista) que tome una lista de números enteros y devuelva dos listas 
ordenadas. La primera con los números pares y la segunda con los números impares.



def separar(lista):
    pares = []
    impares = []
    for numero in lista:
        if numero % 2 != 0:
            impares.append(numero)
        else:
            pares.append(numero)
    pares.sort()
    impares.sort()
    return [pares, impares]

pares, impares = separar([7,2,8,4,9,3,1,6,5])

print(pares)
print(impares)

"""

# ********************************************************

"""
Ejercicio 4: 
   Se necesita solicitar al usuario el ingreso de datos como nombre, edad, dirección y teléfono. Estos 
datos deben ser almacenados en un diccionario llamado usuario_info. Además, se debe permitir el 
ingreso de información para varios usuarios. Finalmente, se requiere mostrar la información 
ingresada por cada usuario en formato clave-valor.



ingresar = True
usuarios = []

while ingresar:
    nombre = input('Ingresar nombre: ')
    edad = int(input('Ingresar edad: '))
    direccion = input('Ingresar direccion: ')
    telefono = input('Ingresar telefono: ')
    
    usuario_info = dict(nombre = nombre, edad = edad, direccion = direccion, telefono = telefono)
    
    usuarios.append(usuario_info)
    
    opcion = input('Desea cargar otro usuario ? (s/n) ')
    if(opcion == 'n'):
        ingresar = False
    borrarPantalla()  
        
print('****** Mostrando informacion de los ususarios ******')
for usuario in usuarios:
    print(usuario)
    print(' ********* ')

"""
# ********************************************************

"""
Ejercicio 5: 
   Localiza el error en el siguiente bloque de código. Crea una excepción para evitar que el programa 
se bloquee y además explica en un mensaje al usuario la causa y/o solución:
resultado = 15 + "20".


# Definimos la excepcion personalizada
class SumaInvalidaException(Exception):
    
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def getMensage(self):
        return self.mensaje
    

try:
    try:
        resultado = 15 + "20"
        print(resultado)
    except TypeError:
        raise SumaInvalidaException('La suma es invalida. No se puede realizar la suma entre numeros y texto. Por favor comprueba que todos los elementos sean numericos')
except SumaInvalidaException as excep:
    print(excep.getMensage())

"""
# ********************************************************

"""
Ejercicio 6:
    Crear una clase Producto con atributos y métodos relacionados con los productos, una clase 
Inventario, la clase Inventario debe tener un atributo de lista para almacenar instancias de la clase 
Producto.
Implementar métodos para agregar un producto al inventario, eliminar un producto del inventario 
y mostrar el inventario actual.
Pruebe la clase Inventario agregando y eliminando productos del inventario y mostrando el 
inventario actualizado


class Producto():
    
    def __init__(self, nombre, marca, precio, stock):
        self.nombre = nombre
        self.marca = marca
        self.precio = precio
        self.stock = stock
        
    def __str__(self):
        return f'''
        Nombre: {self.nombre}
        Marca: {self.marca}
        Precio: {self.precio}
        Stock: {self.stock}
        '''


class Inventario():
    def __init__(self):
        self.listado_productos = []

    def agregar_producto(self, producto):
        self.listado_productos.append(producto)

    def eliminar_producto(self, nombre):
        for producto in self.listado_productos:
            if nombre == producto.nombre:
                self.listado_productos.remove(producto)
                break
    
    def mostrar_inventario(self):
        print(f' ***** INVENTARIO: Cant. productos: {len(self.listado_productos)} *****')
        for producto in self.listado_productos:
            print(producto)
    
inventario = Inventario()

producto1 = Producto('Gaseosa 2 lts','Coca-Cola', 799.99, 15)
producto2 = Producto('Arroz','Gallo', 349.99, 12)
producto3 = Producto('Gaseosa 3 lts','Coca-Cola', 999.99, 15)
producto4 = Producto('Gaseosa 2.5 lts','Pepsi', 899.99, 5)
producto5 = Producto('Crema dental 100 gr','Colgate', 599.99, 5)
producto6 = Producto('Yerba 500 gr','Playadito', 699.99, 10)


inventario.agregar_producto(producto1)
inventario.agregar_producto(producto2)
inventario.agregar_producto(producto3)
inventario.agregar_producto(producto4)
inventario.agregar_producto(producto5)
inventario.agregar_producto(producto6)

inventario.mostrar_inventario()

inventario.eliminar_producto('Crema dental 100 gr')

inventario.mostrar_inventario()

inventario.eliminar_producto('Arroz')

inventario.mostrar_inventario()

"""