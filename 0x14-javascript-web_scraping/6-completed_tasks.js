#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const resJson = JSON.parse(body);

    const users = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
    const dict = {};
    for (const i of users) {
      let count = 0;
      for (const j of resJson) {
        if (i === j.userId && j.completed === true) {
          count++;
        }
      }
      dict[i] = count;
    }
    for (const i in dict) {
      if (dict[i] === 0) {
        delete dict[i];
      }
    }
    console.log(dict);
  }
});
