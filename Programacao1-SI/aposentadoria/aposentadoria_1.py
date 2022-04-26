# Variáveis
def main() :
    idade = int(0);
    tpo_contr = int(0);
    soma = int(0)
    sexo = str('');

    sexo = input('Digite seu Sexo: ');
    idade = int(input('Digite Sua Idade: '));
    tpo_contr = int(input('Digite seu Tempo de Contribuição: '));
    soma = idade + tpo_contr;

# Inicio
    if sexo == 'm':
        if idade >= 65 :
            if tpo_contr >= 15 :
                if soma >= 95 :
                    print("Pode Aposentar");
                else:
                    print('Não pode Aposentar');
            else:
                print('Não pode Aposentar');
        else:
            print('Não pode Aposentar');


    if sexo == 'f':
        if idade >= 60 :
            if tpo_contr >= 15 :
                if soma >= 85 :
                    print("Pode Aposentar");
                else:
                    print('Não pode Aposentar');
            else:
                print('Não pode Aposentar');
        else:
            print('Não pode Aposentar');
# Fim_Algoritmo

if __name__ == "__main__":
    main()



