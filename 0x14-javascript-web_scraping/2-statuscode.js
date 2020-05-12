#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (err, resp) {
  if (err) throw err;
  console.log('code: ' + resp.statusCode);
});
