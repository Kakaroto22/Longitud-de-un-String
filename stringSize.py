import random

def longitudString(str):
	longitud = random.randrange(0, 100)
	while longitud != len(str):	
		longitud = random.randrange(0, 100)
	return longitud
