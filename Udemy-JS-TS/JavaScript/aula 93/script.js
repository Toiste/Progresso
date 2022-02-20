function pessoa(nome, sobrenome) {
    this.nome = nome
    this.sobrenome = sobrenome
}

pessoa.prototype.nomeCompleto = function(){
    return this.nome + ' ' + this.sobrenome;
}

const pessoa1 = new pessoa('Lucas', 'Rezende')
const pessoa2 = new pessoa('Mateus', 'Ribeiro')

console.log(pessoa1.nomeCompleto())

