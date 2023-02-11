function fib(n)
  if n<3 then
    return 1
  else
    return fib(n-1)+fib(n-2)
  end
end

io.write(0,"\n")
for n= 1,19 do
  io.write(fib(n),"\n")
end
io.write("\nProcess finished.")