#!/usr/bin/node

const fs = require('fs');

fs.readFile(process.argv[2], function (error1, data1) {
  if (error1) {
    console.log(error1);
    return;
  }

  fs.readFile(process.argv[3], function (error2, data2) {
    if (error2) {
      console.log(error2);
      return;
    }

    const combinedData = data1 + '\n' + data2;

    fs.writeFile(process.argv[4], combinedData, function (error3) {
      if (error3) {
        console.log(error3);
      }
    });
  });
});
