#!/usr/bin/node
'use strict';

const arg1 = process.argv[2];
const number = Number(arg1);

if (Number.isNaN(number)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${number}`);
}

