//Some todos os Numeros (reduce)
//Retorne um array com os pares (Filter)
//Retorne um array com o dobro dos valores (map)

const numeros = [5, 10, 15, 8, 7, 6, 2, 50, 60, 80]
const total = numeros.reduce(function(acumulador, valor){
    if (valor % 2 === 0) {
        acumulador += valor;
    }
    return acumulador
}, 0);
console.log(total)

//Retorne a Pessoa Mais Velha
const pessoas = [
    {nome: 'Mariana', idade: 62},
    {nome: 'Lucas', idade: 18},
    {nome: 'Otavio', idade: 22},
    {nome: 'Fernando', idade: 42},
    {nome: 'Viv', idade: 17},
];
const maisVelha = pessoas.reduce(function(acumulador, valor) {
    if (acumulador.idade > valor.idade) return acumulador;
    return valor;
});
console.log(maisVelha)