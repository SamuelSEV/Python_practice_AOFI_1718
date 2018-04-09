numero=0
dato1=int(input("Dime un numero mayor que 0:\n"))
if numero > 0:
	numero=dato1
dato2=int(input("Dime un numero mayor que el anterior:\n"))
if numero > dato1:
	numero=dato2
dato3=int(input("Dime un numero menor que 0:\n"))
if numero < 0:
	numero=dato3
resultado=dato1+dato2+dato3
print (dato1, "+", dato2, "+", dato3, "=", resultado)
