 #! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  20221BSI0153.py
#  
#  Copyright 2022
#  Marllon Christiani dos Santos Ribeiro
#  20221BSI0153

# OBS:(considerando que as turmas encerram quando uma turma com identificação igual à string
#  FIM for fornecida pelo usuário de seu programa).
# Para cada aluno da disciplina Programação de Computadores deste semestre. será digitada uma linha
# com:
# • a identificação da turma (A.B, ...• R, nesta ordem);
# • número de matricula;
# • nota final.
# , Após o último aluno de cada turma. virá uma linha. que não corresponde a nenhum aluno, contendo
# zero no lugar do número de matricula. Deseja-se, através de um computador. ler estas linhas e imprimir.
# para cada turma, a sua identificação, o número de alunos aprovados (nota final 60), a média das notas
# e a melhor nota. Após todas as turmas serem processadas. deseja-se imprimir também o total de alunos
# aprovados. a média geral e a melhor nota na disciplina. neste semestre.
# Em problemas deste tipo. sugere-se pensar primeiro em um nível mais geral (disciplina) e depois,
# gradalivamente. em níveis mais particulares (turma. aluno). Em cada nível. deverá haver. quando necessário. uma parte inicial. uma parle intermediária e uma parte final. que terão de ser repetidas ou não. No
# caso de se repetir, deverá existir uma condição de interrupção.


# ALGORITMO
#     declare
#         contadorTurma = int(0)
#         alunos = int(0)
#         notafinal = float(0.0)
#         alunosAprovados = int(0)
#         notaAlunos = float(0.0)
#         melhorNota = float(0.0)
#         mediaNotas = float(0.0)
#         totalAlunosAprovados = int(0)
#         somaMediaNotas = float(0.0)
#         melhorNotaGeral = float(0.0)
#         NUMÉRICO
#     declare
#         turma = str("")
#         matricula = str("")
#         LITERAL
#     melhorNota <- float(-1.0)
#     LEIA turma
#     ENQUANTO turma != "FIM"
#         contadorTurma <- contadorTurma + 1
#         LEIA matricula
#         ENQUANTO matricula != "0"
#             alunos <- alunos + 1
#             LEIA notafinal
#             notaAlunos <- notaAlunos + notafinal
#             SE notafinal >= 60
#             entao alunosAprovados <- alunosAprovados + 1
#                   totalAlunosAprovados <- totalAlunosAprovados + 1
#             FIM SE
#             SE notafinal > melhorNota
#             entao melhorNota <- notafinal
#             FIM SE
#             SE notafinal > melhorNotaGeral
#             entao melhorNotaGeral <- notafinal
#             FIM SE
#             LEIA matricula
#         FIM ENQUANTO
#         SE notaAlunos > 0
#         entao mediaNotas <- notaAlunos/alunos
#                 somaMediaNotas <-  somaMediaNotas + mediaNotas
#         FIM SE
#         SE alunos == 0
#         entao ESCREVA "Turma Vazia"
#         SE NAO  ESCREVA turma
#                         alunosAprovados
#                         mediaNotas
#                         melhorNota
#         FIM SE
#         alunosAprovados <- 0
#         mediaNotas <- 0
#         notaAlunos <- 0
#         melhorNota <- 0
#         alunos <- 0
#         LEIA turma
#     FIM ENQUANTO
#     SE contadorTurma > 0
#     entao mediaGeral <- somaMediaNotas/contadorTurma
#             ESCREVA totalAlunosAprovados
#                     mediaGeral
#                     melhorNotaGeral
#     SE NAO ESCREVA "Não a dados para Processar"
#     FIM SE
# FIM ALGORITMO

                






# Definição do programa principal ou função principal
def main():
    #Declaração de Variaveis.
    turma = str("")
    contadorTurma = int(0)
    matricula = str("")
    alunos = int(0)
    notafinal = float(0.0)
    alunosAprovados = int(0)
    notaAlunos = float(0.0)
    melhorNota = float(-1.0)
    mediaNotas = float(0.0)
    totalAlunosAprovados = int(0)
    somaMediaNotas = float(0.0)
    melhorNotaGeral = float(0.0)
    
    #Iniciação de Variaveis
    turma = input()

    #Processamento
    while turma != "FIM":
        contadorTurma +=1
        matricula = input()

        while matricula != "0":
            alunos += 1
            notafinal = float(input())
            notaAlunos += notafinal

            if notafinal >= 60:
                alunosAprovados += 1
                totalAlunosAprovados +=1
            if notafinal > melhorNota:
                melhorNota = notafinal;
            if notafinal > melhorNotaGeral:
                melhorNotaGeral = notafinal;
            matricula = input();

        if notaAlunos > 0:   
            mediaNotas = notaAlunos/alunos
            somaMediaNotas += mediaNotas
        if alunos == 0:
            #Saida de Dados
            print("Turma Vazia")
        else:
            #Saida de Dados
            print(f"a turma é:{turma}")
            print(f"a quantidade de alunos aprovados é: {alunosAprovados}")
            print(f"a media das notas é: {mediaNotas}")
            print(f"a melhor nota é: {melhorNota}")
        alunosAprovados = 0
        mediaNotas = 0
        notaAlunos = 0
        melhorNota = 0
        alunos = 0
        turma = input()
    
    if contadorTurma > 0:
        mediaGeral = somaMediaNotas/contadorTurma
        #Saida de Dados
        print(f"o total de alunos aprovados é: {totalAlunosAprovados}")
        print(f"a media geral das ntoas é: {mediaGeral}")
        print(f"a melhor nota de todas é: {melhorNotaGeral}")
    else:
        #Saida de Dados
        print("Não a dados para Processar")
        

    # Invocação(execução) do programa principal ou da função principal
if __name__ == "__main__":
    main()