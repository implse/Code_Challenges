/*
Count number of the lowercase vowel letters in the string.
Vowel letters - a, e, i, o, u
*/

var str = "Today is best day of my life";

function vowelsCount(str) {
  let vowels = ["a", "e", "i", "o", "u"];
  let count = 0;
  for (let s of str) {
    if (vowels.includes(s)) {
      count++;
    }
  }
  return count;
}


console.log(vowelsCount(str));
// 8
