import time
numero=int(input("Dime un numero para cuenta atras:\n"))
print ()
for i in range(numero):
	print (numero)
	time.sleep (0.5)
	numero-=1
print (numero, "¡¡¡DESPEGANDO!!!")