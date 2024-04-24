#!/usr/bin/node

const request = require('request');

const filmId = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request.get(filmId, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const resJson = JSON.parse(body);
  console.log(resJson.title);
});
