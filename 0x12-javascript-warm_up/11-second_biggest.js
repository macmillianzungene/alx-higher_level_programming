#!/usr/bin/node

function secondLargest(args) {
  if (args.length <= 1) {
    return 0;
  }

  let largest = -Infinity;
  let secondLargest = -Infinity;

  for (const arg of args) {
    const num = Number(arg);
    if (num > largest) {
      secondLargest = largest;
      largest = num;
    } else if (num > secondLargest && num < largest) {
      secondLargest = num;
    }
  }

  return secondLargest;
}

const args = process.argv.slice(2);
console.log(secondLargest(args));

