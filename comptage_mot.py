#! /usr/bin/python3
#coding:utf-8

# Transformation de la string en list afin de récupérer chaque élément, nous allons ensuite les triés par ordre alphabétique pour pouvoir les compter.
text = ""
while True:
	try:
		text += input()
		text += " "
	except EOFError:
		break
text = text.split(' ')
text.sort()
count = 0
i = 0

# Création d'une boucle pour parcourir toute la list

while i < len(text)-1:
	count += 1

# Boucle pour compter le nombre de récurrence.

	while text[i] == text[i+1]:
		if i < len(text)-2:
			count += 1
			i += 1
		else:
			count += 1
			break

# Affichage du nombre de récurrence avec le mot concerné et getion d'eureur afin d'éviter le comptage d'espace.

	i += 1
	if text[i-1] != '':
		print(count, text[i-1])
		count = 0
	else:
		count = 0

# Gestion d'erreur pour le dernier element de la list afin de le comptabiliser.

if text[i-1] != text[i]:
	count += 1
	print(count, text[i])
