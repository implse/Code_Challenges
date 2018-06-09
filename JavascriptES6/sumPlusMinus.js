/*
Create a function sumPlusMinus() that takes array
and sums separately positive and negative numbers.

It should return an object like this:
{
  plus: 74, // sum of all positive numbers
  minus: -54 // sum of all negative numbers
}
*/

var nums = [10, -12, 30, -1, -8, 0, 14, -33, 20];

function sumPlusMinus(nums) {
  return nums.reduce((acc, e) => {
    return {
      plus: e > 0 ? acc.plus + e : acc.plus,
      minus: e < 0 ? acc.minus - e : acc.minus
    };
  }, {plus: 0, minus: 0});
}

console.log(sumPlusMinus(nums));
// {plus: 74, minus: -54}
