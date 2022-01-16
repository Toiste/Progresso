function verificar(){
    var inicio = document.getElementById('inicio')
    var fim = document.getElementById('fim')
    var passo = document.getElementById('passo')
    var res = document.getElementById('res')
    var mat1 = Number(inicio.value)
    var mat2 = Number(fim.value)
    var mat3 = Number(passo.value)

    if (inicio.value.length == 0 || fim.value.length == 0 || passo.value.length == 0) {
        window.alert('[ERRO] Você não preencheu todos os Dados')
    } else if ( Number(fim.value) < Number(inicio.value) || Number(passo.value) === 0) {
        window.alert('[ERRO] Os valores não são pássiveis de cálculo')
        } else {
            res.innerHTML = `Contando: `
        for ( ;mat1 <= mat2; mat1 += mat3){
            res.innerHTML += `${mat1} \u{1F449}`
        }
        res.innerHTML += `\u{1F3C1}`
    }
} /* a diferença do while pro for é que o for não deixa o valor passar. como exemplificado nesse contador.*/