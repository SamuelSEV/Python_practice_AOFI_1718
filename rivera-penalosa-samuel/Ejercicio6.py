import time
numeropar=0
multiplo3=0
menu="si"
while menu =="si":
	numeropar=int(input("Dime un Nº:\n"))
	if numeropar%2==0:
		multiplo3=numeropar
		print ("PAR")
		time.sleep (1)
	else:
		print ("IMPAR")
		time.sleep (1)
	if multiplo3%3==0:
		print ("Multiplo de 3")
		time.sleep (1)
	else:
		print ("No es multiplo de 3")
		time.sleep (1)
	menu=input("¿Quieres continuar? (si o no)\n")
	if menu != "si":
		print ("hasta luego")

