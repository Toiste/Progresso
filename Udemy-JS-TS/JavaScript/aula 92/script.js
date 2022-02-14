const produto = { nome: 'Produto', preco: 18 };
const caneca = Object.assign({}, produto, {material:'porcelana' });
Object.defineProperty(produto, 'nome', {
    writable: false
})
console.log(Object.getOwnPropertyDescriptor(produto, 'nome'))
console.log(Object.keys(produto))