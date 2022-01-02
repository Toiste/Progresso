function verificar() {
    var nome = document.getElementById('textname')
    var sobrenome = document.getElementById('textsname')
    var data = new Date()
    var ano = data.getFullYear()
    var mes = data.getMonth()
    var dia = data.getDay()
    var fano = document.getElementById('number3')
    var fmes = document.getElementById('number2')
    var fdia = document.getElementById('number')
    var res = document.getElementById('res')
    var idade = ano - Number(fano.value) 

    if (idade < 18) {
        tipo = 'MENOR DE IDADE'
    } else {
        tipo = 'MAIOR DE IDADE'
    }
    if (fano.value.length == 0 || Number(fano.value)  > ano) {
        window.alert('[ERRO] DATA INVÁLIDO! ')

    } else if (fmes.value.length == 0 || Number(fmes.value) > 12 )  {
        window.alert('[ERRO] DATA INVÁLIDO')

    } else if (fdia.value.length == 0 || Number(fmes.value) > 30 )  {
        window.alert('[ERRO] DATA INVÁLIDO')

    } else if (nome.value == 0) {
        window.alert('[ERRO] NOME INVÁLIDO')

    } else if (sobrenome.value == 0) {
        window.alert('[ERRO] SOBRENOME INVÁLIDO')

    } else if ( mes <= Number(fmes.value) && dia < Number(fdia.value)) {
        ano -= 1 
        res.innerHTML = `|Nome:${nome.value} |Sobrenome:${sobrenome.value} | Data de nascimento: ${fdia.value}/${fmes.value}/${fano.value} | Idade: ${idade}  `

    }else { 
        res.innerHTML = `|Nome:${nome.value} |Sobrenome:${sobrenome.value} | Data de nascimento: ${fdia.value}/${fmes.value}/${fano.value} | Idade: ${idade} | ${tipo} `
    
    }
}