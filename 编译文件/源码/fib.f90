function isPrime(n) result(res)
integer (kind= 16),intent (in)::n
logical :: res,NotFound
integer(kind= 16) :: i
NotFound= .true.
if(n<= 3) then
  res= (n>1)
else
 if(mod(n,2)== 0 .or. mod(n,3)== 0)then
  res= .false.
else
i= 5
do while((i*i)<=n)
if(mod(n,i)== 0 .or. mod(n,i+2)== 0 )then
 NotFound= .false.
 res=.false.
 exit
 end if
 i= i+6
 end do
 if(NotFound) then
 res= .true.
   end if
  end if
 end if
end function isPrime

program fib
implicit none
integer(kind= 16)::a = 0,b= 1,c
integer(kind= 16)::v
logical , external :: isPrime
do v= 1,40000
c= b
b= b+a
a= c
if(isPrime(a)) then
print*,"Prime Fibonacci:",a,"Index:",v
  end if
 end do
end program fib