#!/usr/bin/node
'use strict';

const arg1 = process.argv[2];
const times = Number(arg1);

if (Number.isNaN(times)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < times; i++) {
    console.log('C is fun');
  }
}

