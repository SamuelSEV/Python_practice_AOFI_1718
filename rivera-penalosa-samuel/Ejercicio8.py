import time
comida=0
dia=0
Almuerzo={}
Cena={}
semana=["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
print ("¿Que comida quiere para esta semana?")
time.sleep(2)
for dia in semana:
		comida=input(dia + ": ¿Que quiere de Almuerzo?\n")
		Almuerzo[dia]=comida
		comida=input(dia + ": ¿Que quiere de Cena?\n")
		Cena[dia]=comida
print("Menu para semana")
time.sleep(2)
for dia in semana:
	print (dia, "-", "Almuerzo:", Almuerzo[dia], "Cena:", Cena[dia])
	time.sleep(2)