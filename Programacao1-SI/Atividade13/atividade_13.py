#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  20221BSI0153.py
#  
#  Copyright 2022
#  Marllon Christiani dos Santos Ribeiro
#  20221BSI0153
# Programa que leia diversos números inteiros maiores ou iguais a zero na base 10, calcule e imprima
# o equivalente deste número na base 16, As entradas e saídas deste programa devem ser feitas no programa
# principal (função main). A conversão do número lido na base 10 para seu respectivo valor na base 16 deverá
# ser implementada/codificada por você programador. Não é permitido o uso de formatação da apresentação
# do número em hexadecimal e não é permitido o uso de nenhum comando/função já existem tem Python para
# realizar a conversão do número da base 10 para a base 16.

# Definição do programa principal ou função principal
def main():
    #Declaração de Variaveis
    base_10 = int(0);
    numbase_10 = int(0);
    resto = int(0);
    base_16 = str("")
    letras = "ABCDEF"
    #Entrada de Dados
    base_10 = int(input());
    #Processamento
    while base_10 >= 0:
        numbase_10 = base_10;

        if base_10 == 0:
            base_16 = str("0")

        while base_10 > 0:
            resto = base_10 % 16;
            base_10 = base_10 // 16;

            if resto <= 9:
                base_16 = str(resto) + base_16;
            else:
                resto = resto - 10;
                base_16 = letras[resto] + base_16;
        
        print(f"BASE10={numbase_10} BASE16={base_16}")
        base_16 = ""
        base_10 = int(input())
    # Invocação(execução) do programa principal ou da função principal
if __name__ == "__main__":
    main()