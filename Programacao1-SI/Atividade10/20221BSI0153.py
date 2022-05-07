#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  20221BSI0153.py
#  
#  Copyright 2022 Marllon Christiani dos Santos Ribeiro
#  

def main():
    #Declaração de Variaveis
    tp1 = float(0);
    tp2 = float(0);
    tp3 = float(0);
    equipe = int(0);
    tempoetapa1 = float(0.0);
    tempoetapa2 = float(0.0);
    tempoetapa3 = float(0.0);
    delta1 = float(0.0);
    delta2 = float(0.0);
    delta3= float(0.0);
    p1 = float(0.0);
    p2 = float(0.0);
    p3 = float(0.0);
    maiorpt = float(0.0);
    maiorequipe = int(0)

    #Entrada de dados
    tp1 = float(input());
    tp2 = float(input());
    tp3 = float(input());
    equipe = int(input());

    while equipe != 9999 :
        #Entrada de dados
        tempoetapa1 = float(input());
        tempoetapa2 = float(input());
        tempoetapa3 = float(input());

        #Processamento
        #Calcula o valor de delta
        delta1 = abs(tp1 - tempoetapa1);
        delta2 = abs(tp2 - tempoetapa2);
        delta3 = abs(tp3 - tempoetapa3);
        
        #Processamento
        #Calcula os pontos
        if delta1 <= 5 :
            if delta1 < 3 :
                p1 = 100;
            else:
                p1 = 80;
        else:
            p1 = 80 - (delta1 - 5)/5 ;

        if delta2 <= 5 :
            if delta1 < 3 :
                p2 = 100;
            else:
                p2 = 80;
        else:
            p2 = 80 - (delta2 - 5)/5 ;
        
        if delta3 <= 5 :
            if delta1 < 3 :
                p3 = 100;
            else:
                p3 = 80;
        else:
            p3 = 80 - (delta3 - 5)/5 ;

        pt = p1 + p2 + p3;
        
        #Saida de Dados
        print(f"EQUIPE={equipe} P1={p1:.2f} P2={p2:.2f} P3={p3:.2f} PT={pt:.2f}");

        #Processamento
        # Equipe com Maior pontuação/ Equipe Vencedora
        if pt > maiorpt :
            maiorequipe = equipe;
            maiorpt = pt;
        equipe = int(input());

    #Processamento
    if maiorequipe == 0 :
        #Saida de Dados
        print(f"SEM EQUIPES CADASTRADAS");
    else:
        #Saida de Dados
        print(f"EQUIPE VENCEDORA={maiorequipe} PONTUACAO TOTAL={maiorpt:.2f}")

if __name__ == '__main__':
    main()
