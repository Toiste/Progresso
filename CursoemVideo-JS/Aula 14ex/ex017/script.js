function gerar() {
    let numero = document.getElementById('number')
    let tabuada = document.getElementById('seltab')

    if (numero.value.length == 0) {
        window.alert('[ERRO]Preencha os dados e tente Novamente')
    } else {
        let num = Number(numero.value)
        let c = 1
        tabuada.innerHTML = ''
        while (c <= 10) {
            let item = document.createElement('option')
            item.text = `${num} x ${c} = ${num*c}`
            tabuada.appendChild(item)
            c++
        }
    }
}
