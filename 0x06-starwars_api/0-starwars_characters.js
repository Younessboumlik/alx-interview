#!/usr/bin/node

const request = require('request');

request('https://swapi-api.alx-tools.com/api/films/3', function (error, response, data) {


console.log(data);

});
