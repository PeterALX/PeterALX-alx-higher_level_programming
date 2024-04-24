#!/usr/bin/env node

dict = require('./dict.js').dict;
d = {};
for (const [k, v] of Object.entries(dict)) {
  if (d[v] === undefined) {
    d[v] = [k];
  } else d[v].push(k);
}
console.log(d);
