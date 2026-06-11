"""   

  Las tuplas se utilizan para almacenar varios elementos en una sola variable.

   Una tupla es una colección ordenada e inmutable .

   Las tuplas se escriben entre paréntesis.


"""
print("\033c")

paises=("Mexico", "Canada", "EUA")
varios=("Hola", True, 33, 3.1416)
print(paises)
print(varios)
for i in paises:
    print(i)

for i in range(0, len(paises)):
    print(paises[i])

i=0
while i<3:
    print(paises[i])
    i+=1
print(f"El pais que ignagura la copa del mundo es: {paises[0]}")    

edades=(23,24,28,20,20,23,24,19,24)
cuantos=edades.count(24)
print(cuantos)

#Crear un programa que me lea un numero y me diga en que posiciones se encuentra

numero=int(input("Dame un numero"))



#Utilizando tuplas
posicion=edades.index(numero)
print(f"El numero {numero} se encontro en la posicion: {posicion}")
posiciones={""}
posiciones.clear()
for i in range(0, len(edades)):
    if edades[i]==numero:
        posiciones.add(i)
posiciones=tuple(posiciones)
for i in posiciones:
    print(f"El numero {numero} se encontro en la posicion: {i}")





# if numero in edades:
#     print("El numero esta en la posicion", edades.index(numero))
# else:
#     print("No encontre el numero")

# for i in range(len(edades)):
#     if edades[i]==numero:
#         print(f"El numero {numero} esta en la posicion", i)

      