function fib_r(n)
  if n<2
    return n
  else
    return fib_r(n-1)+fib_r(n-2)
  end
end
#println(fib_r(10))
function multi_i(x,y)
  counter= 0
  for i in 1:x
    counter+= y
  end
  return counter
end
#print(multi_i(2,9))
function multi_r(x,y)
  if x== 1
    return y
  else 
    return y+multi_r(y,x-1)
  end
end
#print(multi_r(3,9))
function fact_r(x)
  if x<= 1
    return 1
  else 
    return big(x)*fact_r(x-1)
  end
end
#print(fact_r(5))
fact_f(x)= reduce(*,1:big(x))
#print(fact_f(5))
function fib(n;first= 0,second= 1)
  fibseq= (Integer)[first,second]
  for i in 1:n
   push!(fibseq,fibseq[end]+fibseq[end-1])
  end
  return fibseq[end-1]
end
#print(fib(10))
function fib_i(n;first= 0,second= 1)
  for i in 1:n
    first,second= second,first+second
  end
  return first
end

function fib_r(n)
  if n<2
    return n
  else
    return fib_r(n-1)+fib(n-2)
  end
end

function fib_m(n,d)
  if n in key(d)
    return d[n]
  else
    d[n]= fib_m[n-1,d]+fib_m[n-2,d]
  end
end

function towerofhanoi(discs,from,to,rods)
  if discs== 0
    println("Move disc from $from to $to")
  else
    towerofhanoi(discs-1,from,rods,to)
    towerofhanoi(1,from,to,rods)
    towerofhanoi(discs-1,rods,to,from)
  end
end
#println(towerofhanoi(1,1,3,2))