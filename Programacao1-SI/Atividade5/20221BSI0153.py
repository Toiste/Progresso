# /usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  20221BSI0153.py
#  
#  Copyright 2022 Marllon Christiani dos Santos Ribeiro
#  


def main():
	a = float(input())
	b = float(input())
	c = float(input())
	delta = float(0.0)
	x1 = float(0.0)
	x2 = float(0.0)
	
	
	if a != 0 :
		delta = b**2 + (-4*a*c)
		if delta >= 0 :
			x1 = (-b + delta**(1/2))/(2*a)
			x2 = (-b - delta**(1/2))/(2*a)
			print("x1 = %.2f"%(x1), "x2 = %.2f"%(x2) )
		else:
			print("NAO TEM SOLUCAO NO DOMINIO DO NUMEROS REAIS")
	else:
		print("NAO EH EQ 2G")

if __name__ == "__main__":
	main()
