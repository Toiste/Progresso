//Dobre os numeros

const numeros = [5, 80 ,40 ,9 ,7 ,50]
const numerosEmDobro = numeros.map(valor => valor*2);
console.log(numerosEmDobro)

//Para cada elemento:
//Retorne apenas uma string com o nome da pessoa
//Remova apenas a chave ''nome'' do objeto
//Adicione uma chave id em cada objeto

const pessoas = [
    {nome: 'Mariana', idade: 62},
    {nome: 'Lucas', idade: 18},
    {nome: 'Otavio', idade: 22},
    {nome: 'Fernando', idade: 42},
    {nome: 'Viv', idade: 17},
]

const nomes = pessoas.map(valor => valor.nome)
const idades = pessoas.map(obj => ({ idade: obj.idade }));

const comIds = pessoas.map(function(obj, indice) {
    const newObj = {...obj}
    newObj.id = indice;
    return newObj;
})
console.log(comIds)