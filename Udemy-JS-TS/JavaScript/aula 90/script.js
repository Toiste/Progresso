//defineProperty - definePropeties
function Produto(nome,preco,estoque) {
    this.nome = nome,
    this.preco = preco,
    this.estoque = estoque,

    Object.defineProperty(this, 'estoque', {
        enumerable: true, // mostra a chave
        value: estoque, //valor
        writable: false, // pode alterar ou nao
        configurable: true //configuravel?
    });
}

const p1 = new Produto('Camiseta', 20, 3);
p1.estoque = 5000
console.log(p1)
console.log(Object.keys(p1))