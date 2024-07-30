#!/usr/bin/node
const request = require('request');
request(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}`, async function (error, response, body) {
  if (error) {
    console.log(error);
  }
  characters = JSON.parse(body).characters;
  for (const character of characters) {
    try {
      const name = await promiserequest(character);
      console.log(name);
    } catch (error) {
      console.log('promise rejected: ', error);
    }
  }
});

function promiserequest (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) reject('wee mafi nini');
      else resolve(JSON.parse(body).name);
    });
  });
}
