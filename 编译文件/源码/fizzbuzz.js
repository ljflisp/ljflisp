//console.log("helloworld")
console.log([ ...Array(100).keys() ]
.map( n => ({
  1: n,
  6:"Fizz",
  10:"Buzz",
  0:"FizzBuzz"
})[Math.pow(n,4)%15]) )