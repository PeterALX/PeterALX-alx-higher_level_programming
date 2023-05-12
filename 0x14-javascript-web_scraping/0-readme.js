#!/usr/bin/node

let fs = require("fs")

args = process.argv

fs.writeFile(args[2], args[3], (err)=>{
	if (err) console.log(err)
})
