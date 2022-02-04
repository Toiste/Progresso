//Atribuição via desestruturação (Arrays)

const numeros = [520, 840, 260, 310, 111, 69];
const [primeironumero, segundonumero, ...resto] = numeros;

console.log(primeironumero,segundonumero);
console.log(resto)

// ... rest, ... spread

const nomes = ["vivi", "meri", "arroz", "feijao"];
const [nome1, , nome3] = nomes;

console.log(nome1, nome3)

const number = [[1, 2, 3], [4, 5, 6], [7, 8, 9]];
const [lista1, lista2, lista3] = number;
console.log(lista1[1])