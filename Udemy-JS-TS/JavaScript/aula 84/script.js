// Filter, map, reduce

// Retorne os números maiores que 10

const numeros = [10, 5, 11, 7, 8, 9, 50, 40];

const numerosFilter = numeros.filter(valor => valor > 10)

console.log(numerosFilter)

// Retorne as pessoas que tem o nome com 5 letras ou mais
//Retorne as pessoas com mais de 50 anos
//Retorne as pessoas cujo  nome termina com a

const pessoas = [
    { nome: 'Lucas', idade: 62},
    { nome: 'Vitoria', idade: 23},
    { nome: 'Maria', idade: 19},
    { nome: 'Elisangela', idade: 25},
    { nome: 'Marlene', idade: 40}
];

const pessoasComNomeGrande = pessoas.filter(obj => obj.nome.length > 5)
const pessoasCom50mais = pessoas.filter(obj => obj.idade >= 50)
const TerminaComA = pessoas.filter(obj => obj.nome.toLocaleLowerCase().endsWith('a'))
console.log(TerminaComA)