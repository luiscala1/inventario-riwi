
nombre= ""
Precio= 0
cantidad= 0

print("=MENU=")

nombre = input("ingresa nombre del producto :")

while not nombre.isalpha():
        print("solo se permiten letras")
        nombre=input("ingresa nombre del producto :")
print("texto valido")       

while True:
    
#pide ingresar precio
    try:
        Precio = float(input("ingresa precio producto:"))
        if Precio <= 0:
            print("El precio debe ser mayor que 0, intenta nuevamente")
            continue
        break
    except ValueError:
          print("solo se aceptan numeros, intenta nuevamente")

    #pide ingresar cantidad


while True:
    try:
        cantidad = int (input("ingresa cantidad producto:"))
        if cantidad <= 0:
            print("cantidad debe ser mayor a 0, intenta nuevamente")
            continue
        break
    except ValueError:
        print("solo se aceptan numeros, intenta nuevamente\n")


        
print("==Factura final==\n")

costo_total= (Precio*cantidad)

print("nombre producto:",nombre)
print("precio producto es:", Precio)
print("cantidad producto es:",cantidad)
print("costo total calculado es:",costo_total)





