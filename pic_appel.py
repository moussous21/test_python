#! /usr/bin/python3
#coding:utf-8

# Transformation de la string en list afin de récupérer chaque élément.
text = ""
while True:
	try:
		text += input()
		text += " "
	except EOFError:
		break

text = text.split(' ')
text.pop()
count = len(text)

# Initialisation de l'id_end qui correspond à l'id de la date de fin d'un appel et l'id_start qui correspond à l'id de la date de début d'un autre appel.
id_end = 0
id_start = 1

# Initialisation des deux durées d'appel pour vérifier si les appels ont été fait en simultané. 
time_1 = text[id_end].split(':')
time_2 = text[id_start].split(':')

# Création d'une boucle qui va parcourir tous les appels afin de comptabiliser les appels passers en simultané. 
while id_end < len(text)-1:
	if time_1[1] < time_2[0]:
		count -= 1
		id_end += 1
		id_start = 0
		time_1 = text[id_end].split(':')
		time_2 = text[id_start].split(':')
	elif id_start < len(text)-1:
		id_start += 1
		time_2 = text[id_start].split(':')
	else:
		id_end += 1
		id_start = 0
		time_1 = text[id_end].split(':')
		time_2 = text[id_start].split(':')

# Affichage du pic d'appels.
print(count)
