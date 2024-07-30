#!/usr/bin/node

const request = require('request');
request(process.argv[2], (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const users = JSON.parse(body);
    const dict = {};
    users.forEach(task => {
      if (task.completed) {
        dict[task.userId] = task.userId in dict ? dict[task.userId] + 1 : 1;
      }
    });
    console.log(dict);
  }
});
