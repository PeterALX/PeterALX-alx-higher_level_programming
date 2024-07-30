#!/usr/bin/node

const request = require('request');
request(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const characters = JSON.parse(body).characters;
    characters.forEach(character => {
      request(character, (_, res, bd) => {
        console.log(JSON.parse(bd).name);
      });
    });
  }
});
