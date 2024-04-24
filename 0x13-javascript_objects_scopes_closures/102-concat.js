#!/usr/bin/node

const fs = require('fs');

const args = process.argv.slice(2);

const text1 = fs.readFileSync(args[0]).toString();
const text2 = fs.readFileSync(args[1]).toString();

fs.writeFileSync(args[2], text1 + text2);
