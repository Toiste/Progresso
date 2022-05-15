#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  20221BSI0153.py
#  
#  Copyright 2022
#  Marllon Christiani dos Santos Ribeiro
#  20221BSI0153

# Tem-se um conjunto de dados contendo a altura e o sexo 
# (masculino, feminino) de 50 pessoas,
# Fazer um algoritmo que calcule e escreva: a maior e a menor 
# altura do grupo, a média de altura das mulheres e o número de 
# homens.

# ALGORITMO
#   declare 
#       quantidadePessoas = int(0);
#       altura = float(0.0);
#       homem = int(0);
#       mulher = int(0);
#       alturaMulheres = float(0.0);
#       maiorAltura = float(0.0)
#       menorAltura = float(0.0)
#       
#       mediaAlturaMulheres = float(0.0);
#       NUMÉRICO
#   declare
#       sexo = str("");
#       LITERAL
#       maiorAltura <- float(-1)
#       menorAltura <- float(1000000000000)
#       LEIA quantidadePessoas
#       REPITA quantidade de vezes contidas em quantidadePessoas
#           LEIA sexo, altura
#           SE sexo == "H"
#           então homem += 1
#           fim se
#           SE sexo == "F"
#           então mulher += 1
#           fim se
#           SE altura > maiorAltura
#           então maiorAltura = altura
#           fim se
#           SE altura < menorAltura
#           então menorAltura = altura
#           fim se
#           SE mulher > 0
#           então mediaAlturaMulheres = alturaMulheres / mulher
#           fim se
#           SE quantidadePessoas > 0
#           então ESCREVA maiorAltura, menorAltura
#                 ESCREVA mediaAlturaMulheres
#                 ESCREVA homem
#           fim se
#       FIM REPITA
# FIM ALGORITMO            



# Definição do programa principal ou função principal
def main():
    #Declaração de Variaveis
    quantidadePessoas = int(0);
    sexo = str("");
    altura = float(0.0);
    homem = int(0);
    mulher = int(0);
    alturaMulheres = float(0);
    mediaAlturaMulheres = float(0.0);

    #iniciação de Variaveis
    maiorAltura = float(-1);
    menorAltura = float(1000000000000);
    quantidadePessoas = int(input());

    #Processamento
    for i in range(quantidadePessoas):
        sexo = input().upper();
        altura = float(input());

        if sexo == "H":
            homem += 1 ;
        if sexo == "F":
            mulher += 1 ;
            alturaMulheres += altura;
        if altura > maiorAltura:
            maiorAltura = altura;
        if altura < menorAltura:
            menorAltura = altura;
    if mulher > 0:
        mediaAlturaMulheres = alturaMulheres / mulher ;
    
    if quantidadePessoas > 0:
        #Saida de Dados
        print(maiorAltura, menorAltura);
        print(mediaAlturaMulheres);
        print(homem);

    # Invocação(execução) do programa principal ou da função principal
if __name__ == "__main__":
    main()