#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  20221BSI0153.py
#  
#  Copyright 2022
#  Marllon Christiani dos Santos Ribeiro
#  20221BSI0153
#
# Faça um programa em Python 3 para resolver o seguinte problema:
# Existem vários conjuntos de três valores reais quaisquer onde se
# deseja fazer uma estatística sobre geometria plana triangular. Cada
# conjunto de três valores reais lidos podem ou não # representar os valores
# dos lados um triangulo, ou seja, os três valores reais lidos poderão ou não
# formar um triângulo. Processe estes conjuntos de três valores a fim de responder
# as # perguntas a seguir e considere que os conjuntos de três valores encerram quando
# for fornecido um conjunto com os três valores reais iguais a zero.


# Definição do programa principal ou função principal
def main():
	#Variaveis
	l1 = float(0.0);
	l2 = float(0.0);
	l3 = float(0.0);
	area = float(0.0)
	areamaior = float(0.0);
	perimetro = float(0.0);
	escaleno = int(0);
	isoceles = int(0);
	equilatero = int(0);
	lado1maior = float(0.0);
	lado2maior = float(0.0);
	lado3maior = float(0.0);
	percntriangulo = float(0.0);
	percstriangulo = float(0.0);
	ntriangulo = int(0);
	striangulo = int(0);
	perequilatero = float(0.0);
	perescaleno = float(0.0);
	perisoceles = float(0.0);
	mequilatero = float(0.0);
	mescaleno = float(0.0);
	misoleces = float(0.0);
	
	l1 = float(input());
	l2 = float(input());
	l3 = float(input());

	
	#Processamento
	while l1 != 0 or l2 != 0 or l3 != 0:
		if l1 < (l2 + l3) and l2 < (l1 + l3) and l3 < (l2 + l1):
			striangulo += 1;
			perimetro = l1 + l2 + l3;

			if l1 == l2 == l3:
				triangulo = "EQUILATERO"
				equilatero += 1
				perequilatero += perimetro;
				
			elif l1 != l2 and l1!= l3 and l2 != l3:
				triangulo = "ESCALENO"
				escaleno += 1
				perescaleno += perimetro;
			else:
				triangulo = "ISOSCELES"
				isoceles += 1
				perisoceles += perimetro;
		
			
			sp = perimetro/2
			area = (sp*(sp - l1)*(sp - l2)*(sp - l3))**0.5;
			#Define o triangulo de maior area
			if area > areamaior:
				areamaior = area;
				lado1maior = l1;
				lado2maior = l2;
				lado3maior = l3;
			#Saida de Dados
			print(f"AREA = {area:.2f} PERIMETRO = {perimetro:.2f} TIPO = {triangulo}");
			
		else:
			#Saida de Dados
			print("NAO TRIANGULO")
			ntriangulo += 1;
			
		l1 = float(input());
		l2 = float(input());
		l3 = float(input());
	
	#Calcula a media dos perimetros dos tipos de triangulo
	if equilatero > 0:
		mequilatero = perequilatero/equilatero;
	if escaleno > 0:
		mescaleno = perescaleno/escaleno;
	if isoceles > 0:
		misoleces = perisoceles / isoceles;
	
	if striangulo > 0:
		#Saida de Dados
		print(f"A maior area = {areamaior:.2f} eh do triangulo: lado1 = {lado1maior:.2f}, lado2 = {lado2maior:.2f} e lado3 = {lado3maior:.2f}");
		print(f"{mequilatero:.2f} eh o perimetro medio dos triangulos equilateros");
		print(f"{misoleces:.2f} eh o perimetro medio dos triangulos isosceles");
		print(f"{mescaleno:.2f} eh o perimetro medio dos triangulos escalenos");
		
	if ntriangulo > 0 or striangulo > 0:
		#Calcula o percentual de triangulos e não triangulos
		percntriangulo = (ntriangulo/(ntriangulo + striangulo))*100;
		percstriangulo = (striangulo/(ntriangulo + striangulo)*100)

		#Saida de Dados
		print(f"Percentual de triangulos = {percstriangulo:.2f}");
		print(f"Percentual de nao triangulos = {percntriangulo:.2f}")
	else:
		print("NAO HA DADOS PARA PROCESSAR")

# Invocação(execução) do programa principal ou da função principal			
if __name__ == "__main__":
	main()