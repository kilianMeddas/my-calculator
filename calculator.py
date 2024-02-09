def sum(a,b):
	return a+b

def realDivi(a,b):
	if b != 0:
		return a/b
	else:
		return "Division par zéro impossible"

def sub(a,b):
	return a-b

def pow(a=2,b):
	return a**b

a = int( input('Entrer un entier: '))
b = int(input('Entrer un second entier: '))
action = input('Quel action voulez-vous faire(division, soustraction, somme ou puissance: ')

if action == 'division':
	realDivi(a,b)
elif action == 'soustraction':
	sub(a,b)
elif action == 'somme':
	sum(a,b)
elif action == 'puissance':
	pow(a,b)
else :
	print('invalide opération')



