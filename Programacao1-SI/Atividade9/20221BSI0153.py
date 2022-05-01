#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  20221BSI0153.py
#  
#  Copyright 2022 Marllon Christiani dos Santos Ribeiro
#  


def main():
    #Declaração de Variaveis
    n_turmas = int(0);
    identificacao = str('');
    quantidadematriculado = int(0);
    matricula = str('');
    frequencia = str('');
    percentualfrequencia = float(0.0);
    maiorpercentual = float(0.0);
    turmamaiorpercentual = float(0.0);
    menorpercentual = float(0.0);
    turmamenorpercentual = float(0.0);
    a = int(0);
    b = int(0);
    contagem = int(0);
    altaausencia = int(0);
    maiorpercentual = -1;
    menorpercentual = 1000;
   
   #Entrada de dados
    n_turmas = int(input());
    
    for a in range(n_turmas):
        identificacao = input();
        quantidadematriculado = int(input());
        contagem = 0
       
        for b in range(quantidadematriculado):
            matricula = input();
            frequencia = input();
            
            #Processamento
            if frequencia == 'A':
                contagem += 1
        
        percentualfrequencia = contagem / quantidadematriculado * 100
       
        if percentualfrequencia > maiorpercentual:
            maiorpercentual = percentualfrequencia
            turmamaiorpercentual = identificacao
       
        if percentualfrequencia < menorpercentual:
            menorpercentual = percentualfrequencia
            turmamenorpercentual = identificacao
       
        if percentualfrequencia > 20:
            altaausencia += 1
        #Saida de Dados
        print(f'TURMA={identificacao} AUSENCIA={percentualfrequencia:.2f}%')
    print(f'TURMA COM MAIOR PORCENTAGEM DE AUSENCIA={turmamaiorpercentual} AUSENCIA={maiorpercentual:.2f}%')
    print(f'TURMA COM MENOR PORCENTAGEM DE AUSENCIA={turmamenorpercentual} AUSENCIA={menorpercentual:.2f}%')
    print(f'{altaausencia} TURMAS COM PORCENTAGEM DE AUSENCIA SUPERIOR A 20%')
    #FIM
if __name__ == '__main__':
    main()
