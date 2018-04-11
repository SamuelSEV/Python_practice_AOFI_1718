import time
palabra=0
var1="s"
lista=[]
while var1=="s":
	palabra=input("Dime una palabra:\n")
	var1=input("¿Quieres seguir?(s/n)\n")
	lista.append (palabra)
for i in lista:
	print (i)
	time.sleep(0.65)