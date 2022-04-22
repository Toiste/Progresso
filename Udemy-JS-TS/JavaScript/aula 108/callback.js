/*Função callback*/

function rand(min, max) {
    min *= 1000;
    max *= 1000;
    return Math.floor(Math.random() * (max - min) + min)
}


function esperaAi(msg, tempo, cb) {
    setTimeout(()=> {
        console.log(msg);
        if (cb) cb();
    }, tempo)
}

esperaAi("Frase 1", rand(1, 3), function() {
    esperaAi("Frase 2", rand(1, 3), function() {
        esperaAi("Frase 3", rand(1, 3));
    });
});
