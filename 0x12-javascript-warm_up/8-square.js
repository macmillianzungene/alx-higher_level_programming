#!/usr/bin/node

const size = process.argv[2];

if (isNaN(size)) {
  console.log('Missing size');
} else {
  const squareSize = parseInt(size, 10);
  for (let i = 0; i < squareSize; i++) {
    console.log('X'.repeat(squareSize));
  }
}

