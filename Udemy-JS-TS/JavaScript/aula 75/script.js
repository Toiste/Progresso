//Factory function
function criaPessoa(nome, sobrenome, a, p) {
    return {
        nome,
        sobrenome,
        nomeCompleto() {
            return `${this.nome} ${this.sobrenome}`
        },
        fala(assunto) {
            return `${this.nome} está ${assunto}.`;
        },
        altura: a,
        peso: p,
        //Getter
        get imc() {
            const indice = this.peso / (this.altura ** 2);
            return indice.toFixed(2);
        }
    };
}

const p1 = criaPessoa('Mateus', 'Ribeiro', 1.8, 80)
console.log(p1.imc);
const p2 = criaPessoa('Maria', 'Clara', 1.7, 70)
console.log(p2.imc);