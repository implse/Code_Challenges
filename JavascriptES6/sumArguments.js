/*
Create a function sum() that will sum all arguments passed to it.
Quantity of the arguments is unknown.
*/

function sum(...args) {
  return args.reduce((accumulator, current) => accumulator + current, 0);
}

console.log(sum(1, 3));
//4

console.log(sum(10, 20, 5));
//35

console.log(sum(2, 5, 80, 1, 10, 12));
//110
