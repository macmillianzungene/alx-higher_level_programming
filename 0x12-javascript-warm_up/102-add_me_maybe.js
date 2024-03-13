#!/usr/bin/node

function incrementAndExecute(number, theFunction) {
  let incrementedNumber = number + 1;
  theFunction(incrementedNumber);
}

incrementAndExecute(5, (number) => console.log(`Incremented number is ${number}`));

