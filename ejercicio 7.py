print ("Sistema de procesamiento matemático para valores NO negativos")
numero1=int(input("digite su primer numero entero no negativo:"))
numero2=int(input("digite su segundo numero entero no negatvo:"))
if numero1 >= 0 and numero2 >=0:
    suma= (numero1) + (numero2)
    print ("la suma de sus numeros es de:")
    if numero1 > numero2:
        resta= (numero1) - (numero2)
        print ("la resta de sus numeros es de:", resta)
    else: ("no se úede realizar la operacion")

    if numero1 >0 and numero2:
        multiplicacion= (numero1)*(numero2)
        print ("laq ultiuplicacion de sus numeros es de", multiplicacion)
    else: print("no se puede realizar la operacion")

    dividir= (numero1)/(numero2)
    print("la division de sus umeros es:", dividir)
else: print("no se pede ralizar la operacion")
