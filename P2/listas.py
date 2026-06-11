print("\033c")

#Ejemplo 1 Crear una lista de numeros e imprimir el contenido
numeros=[23,33,45,8,24,0,100]
print(numeros)
lista=""

for i in numeros:
    #lista=lista+","+str(i)
    lista+=f"{i},"
print("["+lista+"]")

for i in range(0,len(numeros)):
    lista+=f"{numeros[i]},"
#print("["+lista+"]")

i=0
while i<len(numeros):
    lista+=f"{numeros[i]},"
    i+=1
print("["+lista+"]")

#Ejemplo 2 Crear una lista de palabras y posteriormente buscar la coincidencia de una palabra 
#1er forma
palabras=["UTD", "tercer","cuatrimestre", "TI"]
palabra=input("Dame la palabra que quieras buscar: ").strip()

if palabra in palabras:
    print(f"Encontre la palabra {palabra} en la lista")
else:
    print(f"No encontre la palabra {palabra} en la lista")    

#2DA FORMA
encontro=False
palabras=["UTD", "tercer","cuatrimestre", "TI"]
palabra=input("Dame la palabra que quieras buscar: ").strip()
for i in palabras:
    if i==palabra:
         
        encontro=True
if encontro:
    print(f"Encontre la palabra {palabra} en la lista")
else:
    print(f"No encontre la palabra {palabra} en la lista")    

#3er FORMA
encontro=False
palabras=["UTD", "tercer","cuatrimestre", "TI"]
palabra=input("Dame la palabra que quieras buscar: ").strip()
for i in range(0, len(palabras)):
    if palabras[i]== palabra:
         
        encontro=True
if encontro:
    print(f"Encontre la palabra {palabra} en la lista")
else:
    print(f"No encontre la palabra {palabra} en la lista")    
#4ta forma
encontro=False
palabras=["UTD", "tercer","cuatrimestre", "TI"]
palabra=input("Dame la palabra que quieras buscar: ").strip()
i=0
while i<len(palabra):
    if i==palabra:
        encontro=True
    i+=1    
if encontro:
    print(f"Encontre la palabra {palabra} en la lista")
else:
    print(f"No encontre la palabra {palabra} en la lista")    

#Ejemplo 3 Añadir elementos a la lista
#opcion 1
lista=[]
true=True
while true:
    valor=input("Dame un valor: ").strip()
    lista.append(valor)
    true=input("Ingresa True/False para continuar: ").strip()
    if true=="False":
        true=False
#opcion 2
continuar="s"
while continuar=="s":
    valor=input("Dame un valor: ").strip()
    lista.append(valor)
    continuar=input("Ingresa s/n para continuar: ").strip().lower()   

  

#Ejemplo 4 Crear una lista multidimensional que permita almacenar el nombre y telefono de una agenda
agenda=[
          ["carlos", "6181234567"],
          ["Adrian", "61812332456"],
          ["Luis", "6182232394"]    

       ]
print(agenda)

for i in agenda:
    print(i)

for r in range(0,3):
    for c in range(0,2):
        print(agenda[r][c])
mensaje=""
for i in range(0,3):
    mensaje+=f"{agenda[i]},"
    print("["+mensaje+"]")
mensaje=""
for r in range(0,3):
    for c in range(0,2):
         mensaje+=f"{agenda[r][c]},"
    mensaje+="\n"     
print(mensaje)          
