def main() :
#Variaveis
    idade = int(0);
    tpo_contr = int(0);
    soma = int(0);
    sexo = str('');

    sexo = input('Digite seu Sexo: ');
    idade = int(input('Digite Sua Idade: '));
    tpo_contr = int(input('Digite seu Tempo de Contribuição: '));
    soma = idade + tpo_contr;
#Inicio
    if sexo == 'm' and idade >= 65 and tpo_contr >= 15 and soma >= 95 :
        print("Pode aposentar");
    else:
        print("Não pode aposentar")


    if sexo == 'f' and idade >= 60 and tpo_contr >= 15 and soma >= 85 :
        print("Pode aposentar");
    else:
        print("Não pode aposentar");
#Fim_Algoritmo

if __name__ == "__main__":
    main()