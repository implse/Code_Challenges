/*
Declare mult() function that will multiply values
of the x, y, z fields of the passed object.
*/

// Object Destructuring
var obj = {
  x: 5,
  y: 20,
  z: 3
};

function multObj(object) {
  let {x, y, z} = object;
  return x * y * z;
}

console.log(multObj(obj));
// 300

// Array Destructuring
var num = [5, 20, 3];

function multArr(arr) {
   let [x, y, z] = arr;
  return x * y * z;
}

console.log(multArr(num));
// 300
