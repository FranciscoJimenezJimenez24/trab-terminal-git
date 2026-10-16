lista = ["pinza", "tijera", "pinza"]
numPinzasEsperadas = 2
contador = 0

for element in lista:
	if element == "pinza":
		contador += 1

if numPinzasEsperadas == contador:
	print(f"Coinciden ambas variables")
elif numPinzasEsperadas < contador:
	print(f"Sobran {contador - numPinzasEsperadas} pinzas")
else:
	print(f"Faltan {numPinzasEsperadas - contador} pinzas")
