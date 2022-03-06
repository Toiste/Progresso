class Pessoa {
    constructor(nome, sobrenome) {
        this.nome = nome;
        this.sobrenome = sobrenome;
    }

    falar() {
        console.log(`${this.nome} está falando`)
    }
}

function pessoa2(nome, sobrenome) {
    this.nome = nome;
    this.sobrenome = sobrenome;
}

pessoa2.prototype.falar = function (){
    console.log(`${this.nome} está falando`)
}

const p1 = new Pessoa('Maria', 'Fernanda')
const p2 = new Pessoa('Lucas', 'Nazare')
const p3 = new pessoa2('Matheus', 'Reginaldo')

console.log(p3, p2)