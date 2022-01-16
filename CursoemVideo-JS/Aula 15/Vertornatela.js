let vetor = [0, 1, 7, 8 ,9]

//for(let pos=0; pos < vetor.length; pos++){
 //   console.log(`A posição ${pos} tem o valor ${vetor[pos]}`)
//}
vetor.indexOf(9) //descobre a posição do valor no vetor.

for(let pos in vetor) {
    console.log(`A posição ${pos} tem o valor ${vetor[pos]}`)
}