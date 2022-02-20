//new Object -> Object.prototype
const objA = {
    chaveA: 'A'
    //__proto__: Object.prototype
};

const objB = {
    chaveB: 'B'
};

const objC = {
    chaveC: 'C'
};

Object.setPrototypeOf(objB, objA);
Object.setPrototypeOf(objC, objA);

