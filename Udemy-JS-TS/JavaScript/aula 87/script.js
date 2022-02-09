//Retorne a soma do dobro de todos os pares
// Filtrar os pares
//Dobrar os valores
//Reduzir (somar tudo)
const numeros = [5,8,50,60,20,4,7,9,13,15]
const numerosPares = numeros
    .filter(valor => valor % 2 === 0)
    .map(valor => valor * 2)
    .reduce((ac, valor) =>  ac + valor);

console.log(numerosPares)