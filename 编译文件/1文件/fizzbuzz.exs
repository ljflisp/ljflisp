mod_pow = fn(base,exp,mod) -> 
:binary.decode_unsigned(:crypto. mod_pow(base,exp,mod))
end

IO.inspect Enum.map 1..100 , &(%{
1 => &1,
6 => "Fizz",
10 => "Buzz",
0 => "FizzBuzz",
}[mod_pow.(&1,4,15)])