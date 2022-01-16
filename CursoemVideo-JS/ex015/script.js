function verificar() {
    var data = new Date()
    var ano = data.getFullYear()
    var fano = document.getElementById('ano')
    var res = document.getElementById('res')
    if (fano.value.length == 0 || Number(fano.value) > ano) {
        window.alert("[ERRO] Verifique os dados e Tente Novamente!")
    } else {
        var fsex = document.getElementsByName('radsex')
        var idade = ano - Number(fano.value)
        var genero = ''
        var img = document.getElementById("img")
        if (fsex[0].checked) {
            genero = 'Homem'
            if (idade >= 0 && idade < 4){
                img.src = "bebehomem.png"
            } else if(idade < 14){
                img.src = "crhomem.png"
            }else if (idade < 21){
                img.src= "jvhomem.png"
            }else if (idade < 50){
                img.src= "jvhomem.png"
            } else {
                img.src= "idoso.png"
            }
        }else if (fsex[1].checked) {
            genero = 'Mulher'
            if (idade >= 0 && idade < 4){
                img.src= "bebemulher.png"
            } else if(idade < 14){
                img.src= "crmulher.png"
            }else if (idade < 21){
                img.src= "jvmulher.png"
            }else if (idade < 50){
                img.src= "jvmulher.png"
            } else {
                img.src= "idosa.png"
            }
        }
        res.innerHTML= `Dectectamos ${genero} com ${idade} anos`
    }
    
}