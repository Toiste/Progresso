const paragrafos = document.querySelector('.paragrafos');
const ps = paragrafos.querySelectorAll('p');

const estilosbody = getComputedStyle(document.body);
const backgroundcolorbody = estilosbody.backgroundColor;

for (let p of ps) {
    p.style.background = backgroundcolorbody
}

