numero=int(input("Dime un numero positivo o negativo:\n"))
tabla=numero
multiplicando=0 	
for x in range(0,11):
	import time
	resultado=tabla*multiplicando
	print (tabla, "*", multiplicando, "=", resultado)
	time.sleep (0.5)
	multiplicando=multiplicando+1
continuar=True
while continuar:
	si=int(input("¿Quieres saber otra tabla?s/n(1 2)\n"))
	if si!=1:
		numero=int(input("Dime un numero positivo o negativo:\n"))
		tabla=numero
		multiplicando=0 	
		for x in range(0,11):
			import time
			resultado=tabla*multiplicando
			print (tabla, "*", multiplicando, "=", resultado)
			time.sleep (0.5)
			multiplicando=multiplicando+1
	if si!=2:
		pass
		print ("hasta luego")