//argumentos que sustentam todos os argumentos enviados
function funcao() {
    let total = 0;
    for (let argumento of arguments) {
        total += argumento
    }

    console.log(total)
}
funcao(1,5,7,8,9,10)

function conta(operador,acumulador, ...numeros){
    for (let numero of numeros) {
        if (operador === '+') acumulador += numero
        if (operador === '-') acumulador -= numero
        if (operador === '/') acumulador /= numero
        if (operador === '*') acumulador *= numero
    }
    console.log(acumulador)
}
conta('+', 0, 20,30,50)