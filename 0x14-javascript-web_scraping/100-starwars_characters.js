#!/usr/bin/node

const request = require('request');

const movieId = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request.get(movieId, function (error, response, body) {
  if (!error) {
    const resJson = JSON.parse(body);
    const people = resJson.characters;
    for (const i of people) {
      request.get(i, function (error, response, body) {
        if (!error) {
          const personName = JSON.parse(body).name;
          console.log(personName);
        }
      });
    }
  }
});
