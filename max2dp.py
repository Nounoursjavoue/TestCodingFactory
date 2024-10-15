max=0

table = [[1,2,3][4,5,6]]

for i in table:
	for element in i :
		if max < element:
			max = element

table = [	[	[1,2,3][4,5,6]   	]
	 	[	[7,8,9][10,11,12]	]
		[	[13,14,15][16,17,18]	]	]


somme = 0
for tab1 in table:
	for tab2 in tab1:
		for n in tab2:
			somme += n

min = 0

emplacement=[]

tabl2d = [[1,2,3][4,5,6]]

for k in tabl2d:
	for el in k:
		if min > el:
			emplacement.append(k)
			emplacement.append(el)
			min = el

matrice  = [[1,2,3][4,5,6]]

for i in matrice:
	for j in i:
		if matrice[i][j] =! matrice[j][i]:
			return print("pas symetrique")


