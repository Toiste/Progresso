const express = require('express');
const route = express.Router();
const homeController = require('./src/controllers/homecontroller')
const contatoController = require('./src/controllers/contatoController')

function meuMiddleware(req, res, next) {
    req.session = {nome: "Marllon", sobrenome: "Ribeiro"}
    console.log();
    console.log('Passei no seu Middleware');
    console.log();
    next();
}

// Rotas da Home
route.get('/', homeController.paginaInicial)
route.post('/', homeController.trataPost);

// Rotas de Contato
route.get('/contato', contatoController.paginaInicial);

module.exports = route;