const date = new Date();
const diames = date.getDate();
const diasemana = date.getDay();
const mes = date.getMonth();
const ano = date.getFullYear();
const horas = date.getHours();
const minutos = date.getMinutes();

function diaseman() {
    let semana;
    switch (diasemana) {
        case 0: semana = "Domingo"
        break;
        case 1: semana = "Segunda-Feira"
        break;
        case 2: semana = "Terça-Feira"
        break;
        case 3: semana = "Quarta-Feira"
        break;
        case 4:semana = "Quinta-Feira"
        break;
        case 5: semana = "Sexta-Feira"
        break;
        case 6: semana = "Sábado"
        break;
    }
    return semana
}

function mesdoano() {
    let m;
    switch (mes) {
        case 0: m = "Janeiro"
        break;
        case 1: m = "Fevereiro"
        break;
        case 2: m = "Março"
        break;
        case 3: m = "Abril"
        break;
        case 4:m = "Maio"
        break;
        case 5: m = "Junho"
        break;
        case 6: m = "Julho"
        break;
        case 7: m = "Agosto"
        break;
        case 8: m = "Setembro"
        break;
        case 9: m = "Outubro"
        break;
        case 10: m = "Novembro"
        break;
        case 11: m = "Dezembro"
    }
    return m
}

function zeroesquerda(num) {
    return num >= 10 ? num : `0${num}`;
}

function time() {
    const texto = document.getElementById("1");
    texto.innerHTML = `${diaseman()}, ${diames} de ${mesdoano()} de ${ano} ${zeroesquerda(horas)}:${zeroesquerda(minutos)}`
}