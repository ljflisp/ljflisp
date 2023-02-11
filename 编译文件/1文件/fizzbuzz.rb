puts (1..100).map{
  |n| {
    1 => n,
    6 => "Fizz",
    10 => "Buzz",
    0 => "FizzBuzz"
  }[n**4%15]
}
#puts "%S".map