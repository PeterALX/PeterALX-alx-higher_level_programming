#!/usr/bin/node

const request = require('request');
request(process.argv[2], (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const films = JSON.parse(body).results;
    let count = 0;
    films.forEach((film) => {
      film.characters.forEach(c => {
        if (c.includes('18')) {
          count++;
        }
      });
    });
    console.log(count);
  }
});
