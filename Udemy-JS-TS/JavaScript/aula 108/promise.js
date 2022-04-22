/*Promises*/

function rand(min, max) {
    min *= 1000;
    max *= 1000;
    return Math.floor(Math.random() * (max - min) + min)
}


/* Se o typeof de msg não for uma string ele é jogado para o catch. Onde o erro é tratado.*/

function esperaAi(msg, tempo) {
    return new Promise((resolve, reject) => {
        if(typeof msg != 'string') reject('BAD VALUE');
        setTimeout(()=> {
            resolve(msg);
        }, tempo)
    });
}

esperaAi('Frase 1', rand(1, 3))
.then(resposta => {
    console.log(resposta);
    return esperaAi( 2, rand(1, 3));
})
.then(resposta => {
    console.log(resposta);
    return esperaAi('frase 3', rand(1, 3))
})
.then(resposta => {
    console.log(resposta);
})
.catch(e => {
    console.log('ERRO', e)
});