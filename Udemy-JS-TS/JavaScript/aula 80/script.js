function* gerador1() {
     //codigo qualquer
     yield 'Valor 1';
     //condigo qualquer
     yield 'Valor 2';
     //codigo qualquer
     yield 'Valor 3';
}

const g1 = gerador1();

function* geradora2() {
    let i = 0;

    while(true) {
        yield i;
        i++;
    }
}
const g2 = geradora2();

function* geradora3() {
    yield 0;
    yield 1;
    yield 2;
}

function* geradora4() {
    yield* geradora3();
    yield 3;
    yield 4;
    yield 5;
}

const g4 = geradora4();
for(let valor of g4) {
    console.log(valor)
}

function* geradora5() {
    yield function() {
        console.log('vim do y1')
    }
}
