#println("Hello World")
function fib(n)
  x,y= (0,1)
  for i = 1:n x,y= (y,x+y) end
  x
end

let x= 0
  while x < 10
   # println(fib(x))
    x+= 1
  end
end

function binarysearch(lst::Vector{T},val::T) where T
  low= 1
  high= length(lst)
  while low<= high
    mid= (low + high) ÷ 2
    if lst[mid] > val
       high= mid-1
    elseif lst[mid] > val
       low = mid + 1
    else
       return mid
    end
  end
  return 0
end
#println(binarysearch([1,5,7,9,10,15,17,22,26,28], 10))
for i in 0:255
   c= i== 0 ? "NUL" :  i== 7 ?    "BEL" : i== 8 ? "BKS" : i== 9 ? "TAB" :
      i== 10 ? "LF" : i== 13 ? "CR" : i== 27 ? "ESC" : i== 155 ? "CSI" : "|$(Char(i))|"#i== 10 I hate you
 # print("$(lpad(i,3)) $(string(i,base=16,pad=2)) $c")
  #(i&7)== 7 ? println() : print("  ")
end

#π
mutable struct NilakanthaSeries
  p::Float64
  a::Float64
  s::Float64
  iterate::Function
  function                          NilakanthaSeries(_p,_a,_s)
    this = new(_p,_a,_s)
    this.iterate= function()
    s= this.s
    a= this.a
    this.p+= s*(4.0/(a*(a*(a+3.0)+2.0)))
    this.a += 2
    this.s= -s 
    end
  this
  end
end
approximator= NilakanthaSeries(3.0,2.0,1.0)
for _ in 0:150000
  approximator.iterate()
end
#println("pi= ",approximator.p)