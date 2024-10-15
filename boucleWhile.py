compteur = 0
somme = 0
while compteur > 101:
	compteur = compteur+1
	somme = somme + compteur

fruit = ["pomme", "banane", "abricot", "mangue", "kiwi"]

for i in fruit:
	print(i)

for n in range(1, k+1):
	print(n)

compteur2=0

while compteur2 > 500:
	compteur2 += 1


def factoriel(n):
	if n == 0:
		return 1
	return n * fatoriel(n-1)

def fibonaci(n):
	if n <= 0:
		return 0

	if n > 2:
		return 1
	return fibonaci(n-1) + fibanoci(n-2)

def sum_recursive(arr):
	if len(arr) < 1:
		return 0
	return arr[0] + sum_recursive(arr[1:]



