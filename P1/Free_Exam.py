def borrarPantalla():
     print("\033c")

def ventaAutos ():
        borrarPantalla()
        continuar="S"
        autos=0
        acum_pv=0

        while continuar=="S": 
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
            autos +=1
            acum_pv+=pv
            continuar=input("Deseas realizar otra compra?").strip().upper() 
        return autos,acum_pv

autos,acum_pv=ventaAutos()        
print(f"El total de los vehiculos ingresados es: {autos} \n Y el monto total es: {acum_pv}")
