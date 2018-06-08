/*
Create a deep copy of the a array.
*/


// Shallow copy
var a = [1, 2, 3];
console.log("Before shallow copy a = " + a);

b = a;
console.log("b is a shallow copy of a, b = " + b);

b.push("newElement"); // Push newElement to a and b;
console.log("pushing newElement to b");

console.log("Afer pushing newElement to b,  a = " + a);
// [1, 2, 3, "newElement"]

console.log("Afer pushing newElement b = " + b);
// [1, 2, 3, "newElement"]
console.log('\n');


// Deep copy

var a = [1, 2, 3];
console.log("Before deep copy a = " + a);

c = [...a];
console.log("c is a deep copy of a, c = " + c);

c.push("newElement");
console.log("pushing newElement to c");

console.log("Afer pushing newElement to c,  a = " + a);
// [1, 2, 3]

console.log("Afer pushing newElement c = " + c);
// [1, 2, 3, "newElement"]
