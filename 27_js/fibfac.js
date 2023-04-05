// Team Phantom Tollbooth :: Clyde Sinclair, Fierce Dragon 
// SoftDev pd0
// K27 -- Basic functions in JavaScript
// 2023-04-04t
// --------------------------------------------------


// as a duo...
// pair programming style,
// implement a fact and fib fxn

var fact = function(n) {
  if (n < 2) {
    return 1;
  } else {
    return n * fact(n - 1);
  }
}

var fib = function(n) {
  if (n == 0) {
    return 0;
  } else if (n == 1) {
    return 1;
  } else {
    return fib(n-1) + fib(n-2);
  }
}

//Do whatever you think is needed. Think: S I M P L E.   Think: S M A R T.

console.log(fact(5));
console.log(fib(5));
