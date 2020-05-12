#!/usr/bin/node
const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/:id' + process.argv[2];
request(url, function (err, resp, body) {
  if (err) throw err;
  console.log(JSON.parse(body).title);
});
