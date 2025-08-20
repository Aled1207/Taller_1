print ("factura")
Precio_base=float(input("valor del producto:"))
iva= (Precio_base *0.16) + Precio_base
print ("valor del producto con iva es de")
if iva > 500000:
    descuento= iva - (iva *0.15)
if iva < 500000:
    descuento= iva
print ("su factura por la compra es de: ", descuento)