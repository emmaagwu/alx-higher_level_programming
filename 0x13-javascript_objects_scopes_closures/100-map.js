#!/usr/bin/node
const { list } = require('./100-data');

const newLi = list.map((x, index, array) => {
  if (index === 0) {
    return 0;
  }
  return (array[index - 1] * x);
});

console.log(list);
console.log(newLi);
