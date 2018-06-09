/*
Swap values of the a and b.
Don't use for this any new variable.
*/

"use strict";

var a = "first";
var b = "second";

// Destructuring
[a, b] = [b, a];

console.log(a, b);
// second first
