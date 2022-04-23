
/* você pode usar o as tanto no Import quanto no export. */
import { nome as nome2, sobrenome as seila, soma, Pessoa } from './modulo1';

console.log(nome2)

console.log(soma(5, 5), seila)

const p1 = new  Pessoa("Lucas", "Santos");

console.log(p1)
