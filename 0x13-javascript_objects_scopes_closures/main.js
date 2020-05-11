#!/usr/bin/node
const converter = require('./10-converter').converter;

const myConverter = converter(20);

console.log(myConverter(5));
console.log(myConverter(10));
console.log(myConverter(100));
