#!/usr/bin/node

const dict = require('./101-data.js').dict;
const d = {};
for (const [k, v] of Object.entries(dict)) {
  if (d[v] === undefined) {
    d[v] = [];
  }
  d[v].push(k);
}
console.log(d);
