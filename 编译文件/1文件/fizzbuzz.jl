for n in 0:100
  println(
    Dict(
      1 =>n,
      6 =>"Fizz",
      10 =>"Buzz",
      0 =>"FizzBuzz"
    )[n^4%15]
  )
end