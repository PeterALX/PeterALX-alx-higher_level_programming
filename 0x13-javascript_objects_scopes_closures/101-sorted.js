#!/usr/bin/env node

const dict = require('./dict.js').dict;
const d = {};
for (const [k, v] of Object.entries(dict)) {
  if (d[v] === undefined) {
    d[v] = [];
  }
  d[v].push(k);
}
console.log(d);
