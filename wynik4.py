# Wyliczanie ciagu fibonacciego

def fibonacci(liczba):
	if liczba == 1:
		return 0
	elif liczba == 2:
		return 1
	else:
		a = 0
		b = 1
		for indeks in range(2, liczba):
			wynik = a + b
			a = b
			b = a + b
			
		return wynik
		
	
for indeks in range(2, 10):
	if indeks < 7:
		print(fibonacci(indeks))
	elif indeks == 9:
		break
	else:
		print(indeks)
		continue
		
	
