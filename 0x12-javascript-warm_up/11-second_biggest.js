#!/usr/bin/node

if (isNaN(process.argv[2]) || !process.argv[2] || process.argv.length < 4) {
  console.log('0');
} else {
  let i = 2;
  const arr = [];

  while (process.argv[i]) {
    arr.push(parseInt(process.argv[i]));
    i++;
  }
  arr.sort((a, b) => b - a);
  console.log(arr[1]);
}
