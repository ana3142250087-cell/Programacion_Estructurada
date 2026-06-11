"""

 
 Sets.- 
  Es un tipo de datos para tener una coleccion de valores pero no tiene ni indice ni orden

  Set es una colección desordenada, inmutable* y no indexada. No hay miembros duplicados.
"""
print("\033c")

set1 = {"hola", "123", 123, "mexico", "Holanda"}

set1.add("ganador")
print(set1)

set1.pop()
print(set1)

# Ejemplo:
# Crear un programa que solicite los email de los alumnos de la UTD, almacenar en una lista y posteriormente mostrar en pantalla los email sin duplicados.

# Solución 1

emails = []
cantidad = int(input("¿Cuántos correos desea ingresar?: "))

for i in range(cantidad):
    correo = input(f"Ingrese el correo {i+1}: ")
    emails.append(correo)

print("\nLista original:")
print(emails)

emails_sin_duplicados = list(set(emails))

print("\nLista sin duplicados:")
print(emails_sin_duplicados)

# Solución 2


emails = []
cantidad = int(input("\n¿Cuántos correos desea ingresar?: "))

for i in range(cantidad):
    correo = input(f"Ingrese el correo {i+1}: ")
    emails.append(correo)

sin_duplicados = []

for correo in emails:
    if correo not in sin_duplicados:
        sin_duplicados.append(correo)

print("\nLista original:")
print(emails)

print("\nLista sin duplicados:")
print(sin_duplicados)
  



