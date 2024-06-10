#!/usr/bin/node
const request = require('request');

function printingCharacters(character) {
    return new Promise((resolve, reject) => {
        request(character, function (error, response, datachar) {
            if(error) {
                console.log('error:', error);
                reject(error);
            }
            else if(response.statusCode !== 200) {
                console.log('statusCode:', response && response.statusCode);
                reject(new Error('Invalid status code: ' + response.statusCode));
            }
            else if(!datachar) {
                console.log('No data returned');
                reject(new Error('No data returned'));
            }
            else {
                let char = JSON.parse(datachar);
                console.log(char.name);
                resolve(char.name);
            }
        });
    });
}

request('https://swapi-api.alx-tools.com/api/films/3', async function (error, response, data) {
    let jsondata = JSON.parse(data);
    let characters = jsondata.characters;

    for (let character of characters) {
        try {
            await printingCharacters(character);
        } catch (error) {
            console.error('Error printing character:', error);
        }
    }
});
