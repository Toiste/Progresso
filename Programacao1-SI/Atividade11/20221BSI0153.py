#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  20221BSI0153.py
#  
#  Copyright 2022 Marllon Christiani dos Santos Ribeiro
#  

import math
def main():
    #Declaração de Variaveis
    n = float(0.0);
    x = float(0.0);
    exp = float(0.0);
    somatorio = float(1.0);
    fat = int(0)
    contador = int(0)
    diferenca = float(1.0)

    #Entrada de Dados
    n = int(input());

    for i in range(n):
        #Entrada de Dados
        x = float(input());

        #calcula Exponencial
        exp = math.exp(x);
        
        #Processamento
        #Calcula a somatoria
        while diferenca >= 0.0001 :
            contador += 1;
            fat = contador;

            for o in range(fat - 1, 0, -1):
                fat *= o

            somatorio += (x**contador)/fat;
            
            diferenca = abs(exp - somatorio);

        #Saida de Dados
        print(f"X={x:.6f} EXP_FUNCAO({x:.6f})={exp:.6f} EXP_SERIE({x:.6f})={somatorio:.6f}")
        #Reseta as Variaveis
        contador = 0;
        somatorio = float(1.0);
        diferenca = 1;
    #Fim
        
if __name__ == '__main__':
    main()