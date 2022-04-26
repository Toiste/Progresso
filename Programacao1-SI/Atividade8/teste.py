segundos = 20000
minutos = 0
horas = 0

while segundos > 60 :
	segundos -= 60 ;
	minutos += 1 ;
	
while minutos > 60 :
    minutos -= 60 ;
    horas += 1 ;


print(horas, minutos, segundos)