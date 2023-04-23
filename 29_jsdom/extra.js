//strict equality vs normal equality
//these are all true, even though they aren't the same type
//appears that values are typecasted and compared
console.log(0 == "0");
console.log(0 == false);
console.log(0 == []);
console.log(false == []);

//these are all false, since they aren't of the same type
console.log(0 === "0");
console.log(0 === false);
console.log(0 === []);
console.log(false === []);

//function keyword
function fib(n) {
    if (n == 0) {
        return 0;
      } else if (n == 1) {
        return 1;
      } else {
        return fib(n-1) + fib(n-2);
      }
}