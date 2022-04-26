# /usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  20221BSI0153.py
#  
#  Copyright 2022 Marllon Christiani dos Santos Ribeiro
#  


def main():
	n1 = int(0)
	n2 = int(0)

	n1 = int(input())
	n2 = int(input())
	divisao = 0

	if n1 > 0 and n2 > 0 :
		while n1 >= n2 :
			n1 = n1 - n2 
			divisao = divisao + 1

		print("QUOCIENTE =[%d]" % divisao)
	else:
		print("ENTRADA INVALIDA")



if __name__ == "__main__":
	main()

