'''
  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- Sin estructuras de control
  2.- Sin funciones

'''
nume=int(input("Ingresa un numero"))
num=1
mult=nume*num
print(f"{nume} X {num} = {mult}")
num+=1
mult=nume*num
print(f"{nume} X {num} = {mult}")
num+=1
mult=nume*num
print(f"{nume} X {num} = {mult}")
num+=1
mult=nume*num
print(f"{nume} X {num} = {mult}")
num+=1
mult=nume*num
print(f"{nume} X {num} = {mult}")
num+=1
mult=nume*num
print(f"{nume} X {num} = {mult}")
num+=1
mult=nume*num
print(f"{nume} X {num} = {mult}")
num+=1
mult=nume*num
print(f"{nume} X {num} = {mult}")
num+=1
mult=nume*num
print(f"{nume} X {num} = {mult}")
num+=1
mult=nume*num
print(f"{nume} X {num} = {mult}")
num+=1
'''
  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- Con estructuras de control
  2.- Sin funciones

'''
print("\033c")


nume=int(input("Ingresa un numero "))
i=100
while i>=10:
    mult=nume*num
    print(f"{nume} X {num} = {mult}")
    i-=1

num=1

while num<=10:
     mult=nume*num
     print(f"{nume} X {num} = {mult}")
     num+=1

for num in range (1,11):
    mult=nume*num
    print(f"{nume} X {num} = {mult}")
    



"""for i in range (100,0,-10):
    mult=nume*num
    print(f"{nume} X {num} = {mult}")
    num+=1"""

print("\033c")
def tabla(tab, num):
    mult=nume*num
    print(f"{tab} X {num} = {mult}")
    num+=1
    return num

nume=int(input("Ingresa un numero "))
numer=1
numer=tabla(nume, numer)
numer=tabla(nume, numer)
numer=tabla(nume, numer)
numer=tabla(nume, numer)
numer=tabla(nume, numer)
numer=tabla(nume, numer)
numer=tabla(nume, numer)
numer=tabla(nume, numer)
numer=tabla(nume, numer)
numer=tabla(nume, numer)

def multi(num):
    num=1
    mult=nume*num
    print(f"{nume} X {num} = {mult}")
    num+=1
    mult=nume*num
    print(f"{nume} X {num} = {mult}")
    num+=1
    mult=nume*num
    print(f"{nume} X {num} = {mult}")
    num+=1
    mult=nume*num
    print(f"{nume} X {num} = {mult}")
    num+=1
    mult=nume*num
    print(f"{nume} X {num} = {mult}")
    num+=1
    mult=nume*num
    print(f"{nume} X {num} = {mult}")
    num+=1
    mult=nume*num
    print(f"{nume} X {num} = {mult}")
    num+=1
    mult=nume*num
    print(f"{nume} X {num} = {mult}")
    num+=1
    mult=nume*num
    print(f"{nume} X {num} = {mult}")
    num+=1
    mult=nume*num
    print(f"{nume} X {num} = {mult}")
    num+=1
multi(num)
"""Restricciones: 
  1.- con estructuras de control 
  2.- Con funciones"""



print("\033c")

def tabla(num_tab,n):
    mul=num_tab*n
    print(f"{num_tab} x {n}  = {mul} ")
    n+=1
    return n
  
num_tabla=int(input("Dame un numero para obtener la tabla de multiplicar:  "))

for num in range(1,11):
  num=tabla(num_tabla,num)


