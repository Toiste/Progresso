/*Promise.all = Retorna todas as promises de um array resolvidas, se uma tiver um erro, todas são rejeitadas.
Promise.race = Retorna a primeira promise resolvida.
Promise.resolve = Retorna uma promise já resolvida.
Promise.reject = Retorna uma promise Rejeitada.
 */

function rand(min, max) {
    min *= 1000;
    max *= 1000;
    return Math.floor(Math.random() * (max - min) + min)
}




function esperaAi(msg, tempo) {
    return new Promise((resolve, reject) => {
        if(typeof msg != 'string') reject('BAD VALUE');
        setTimeout(()=> {
            resolve(msg);
        }, tempo)
    });
}

function baixaPagina() {
    const emCache = true;

    if(emCache) {
        return Promise.reject('Página em cache')
    }else {
        return esperaAi('Baixei a pagina', 3000);
    }
}

baixaPagina()
.then(dadosPagina => {
    console.log(dadosPagina);
})
.catch(e => console.log('Erro', e))