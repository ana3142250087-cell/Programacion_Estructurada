
continuar=input("Deseas continuar").upper()



marca=input("Marca: ").strip().upper()
origen=input("Origen: ").strip().upper()
costo=float(input("Costo: "))
impuesto=0
if origen=="ALEMANIA":
    impuesto=0.20
elif origen=="JAPON":
    impuesto=0.30
elif origen=="ITALIA":
    impuesto=0.15
elif origen=="USA":
    impuesto=0.08
impuesto_pesos=costo*impuesto
pv=impuesto_pesos+costo
print(f"El impuesto pagar es: $ {impuesto_pesos}")
print(f"El precio de venta es: $ {pv}")


