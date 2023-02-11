print([
     (lambda n :{
       1:n,
       6:"Fizz",
       10:"Buzz",
       0:"FizzBuzz"
     }[n**4%15])(n+1)
     for n in range(100)
])