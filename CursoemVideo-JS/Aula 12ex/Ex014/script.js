function carregar() {
    var msg = document.getElementById('msg')
    var img = document.getElementById('img')
    var data = new Date()
    var hora = data.getHours()

    msg.innerHTML = `agora são ${hora} Horas`
    if (hora >= 0 && hora < 12) {
        img.src = 'manha.png'
        document.body.style.background = '#4d3c60'
    } else if (hora >= 12 && hora < 18){
        img.src = 'tarde.png'
        document.body.style.background = '#976163'
    } else {
        img.src = 'noite.png'
        document.body.style.background = '#eeeae7'
    }
}
