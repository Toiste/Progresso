// function hoisting
falaoi();
function falaoi() {
    console.log('Oi');
}

//First-class objects (Objetos de primeira classe)
//
const souUmDado = function() {
    console.log('sou um dado');
}
souUmDado();

function executaFuncao(funcao) {
    funcao()
}
executaFuncao(souUmDado);

//arrow function
const funcaoarrow = () => {
    console.log('sou uma arrow function')
};
funcaoarrow();

// Dentro de um objeto
const obj = {
    falar() {
        console.log('estou falando')
    }
};
obj.falar()