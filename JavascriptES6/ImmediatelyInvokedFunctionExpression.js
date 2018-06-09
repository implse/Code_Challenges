/*
Complete IIFE (Immediately Invoked Function Expression) that will expose following methods:
  greet() - It will take one argument and return greeting string
  changeGreeting() - It will change greeting string

Initial greeting string "Hey, that's" must be defined inside IIFE.
*/

// var greeting = (Write IIFE here);
var greeting =(() => {
  var greetingString = "Hey, that's";

  function greet(name) {
    return `${greetingString} ${name}`;
  }

  function changeGreeting(newGreeting) {
    greetingString = newGreeting;
  }

  return {greet, changeGreeting};
})();

console.log(greeting.greet("Bob"));
// Hey, that's Bob

greeting.changeGreeting("Good Morning from")


console.log(greeting.greet("Emily"));
// Good Morning from Emily
