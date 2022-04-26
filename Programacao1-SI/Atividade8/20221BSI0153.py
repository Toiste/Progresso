# /usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  20221BSI0153.py Aqui Entra o Nome do Arquivo do Código fonte
#  
#  Copyright 2022 Marllon Christiani dos Santos Ribeiro
#  


def main():
	massa = float(0.000)
	massa = float(input())
	texto = ""
	segundos = int(0)
	minutos = int(0)
	horas = int(0)

	if massa >= 0 :
		while massa >= 0 :
			texto += (f"MASSA INICIAL={massa:.3f}")
			#CALCULA A DIVISAO DA MASSA E A CONTAGEM DO TEMPO
			while massa >= 0.5 :
				massa = massa/2 ;
				segundos += 50 ;
			# CALCULA OS SEGUNDOS E MINUTOS
			while segundos >= 60 :
				segundos -= 60 ;
				minutos += 1 ;
			#CALCULA OS MINUTOS E AS HORAS
			while minutos >= 60 :
				minutos -= 60 ;
				horas += 1 ;
			#Arredonda a massa final
			massaFinal = round(massa, 3)
			texto += (f" MASSA FINAL={massaFinal:.3f} TEMPO DECORRIDO={horas}:{minutos}:{segundos}\n") ;
			massa = float(input())
			#Reseta o Tempo
			segundos = int(0)
			minutos = int(0)
			horas = int(0)
		texto += "FIM"
		print(texto)
		

	else:
		print("FIM");
	
		


if __name__ == "__main__":
	main()

