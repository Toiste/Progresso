let tab = document.querySelector('select#tabela')
let numero = document.querySelector('input#number')
let res = document.querySelector('div#res')
let valores = []

function isNumero(n){
    if (Number(n) >= 1 && Number(n) <= 100){
        return true
    } else {
        return false
    }
}

function inLista(n, l){
    if (l.indexOf(Number(n)) != -1){
        return true
    } else {
        return false
    }
}

function adicionar(){
    if (isNumero(numero.value) && !inLista(numero.value, valores)){
        let item = document.createElement('option')
        item.text = `o Valor ${numero.value} Foi Adicionado`
        tab.appendChild(item)
        valores.push(Number(numero.value))
        res.innerHTML = ''
    } else {
        alert('[ERRO] Valor inválido ou já encontrado em Lista')
    }
    numero.value = ''
    numero.focus()
}


function verificar(){
    if (valores.length == 0){
        alert(`[ERRO]`)
    } else {
        let quant = 0
        let maior = valores[0]
        let menor = valores[0]
        let media = 0
        for (let pos in valores){
            quant += valores[pos]
            if (valores[pos] > maior)
                maior = valores[pos]
            if (valores[pos] < menor)
                menor = valores[pos]
        }
        media = quant/valores.length
        res.innerHTML += ``
        res.innerHTML += `<p>O maior Valor informado foi ${maior}</p>`
        res.innerHTML += `<p>O menor Valor informado foi ${menor}</p>`
        res.innerHTML += `<p>Somando todos os Valores, temos ${quant}</p>`
        res.innerHTML += `<p>A média dos Valores Digitados é ${media}</p>`
    }
}