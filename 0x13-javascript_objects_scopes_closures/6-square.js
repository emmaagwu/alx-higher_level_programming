#!/usr/bin/node

const square = require('./5-square');

class Square extends square {
  charPrint (c) {
    let string = '';
    if (c) {
      for (let i = 0; i < this.width; i++) {
        string += c;
      }
    } else {
      for (let i = 0; i < this.width; i++) {
        string += 'X';
      }
    }
    for (let i = 0; i < this.height; i++) {
      console.log(string);
    }
  }
}

module.exports = Square;
