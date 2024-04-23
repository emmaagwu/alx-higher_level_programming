#!/usr/bin/node

const request = require('request');

const fs = require('fs');

const file = process.argv[3];

request.get(process.argv[2], function (error, response, body) {
  if (!error) {
    fs.writeFile(file, body, error => {
      if (error) {
        console.log(error);
      }
    });
  }
});
