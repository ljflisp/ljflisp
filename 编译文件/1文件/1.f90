function fact(n) result(res)
    integer ,intent(in)::n
    integer :: res
    integer :: accumulator

    integer :: v
    accumulator= 1
    do v= 1,n
    accumulator= accumulator*v
    end do
    res= accumulator
    end function fact

program Euler
     implicit none

     integer ,external ::fact
     integer ,parameter ::dp= kind(0.q0)
     real(dp) :: res= 0_dp
     integer :: i = 0
     real(dp) :: test= 0_dp

     do while (test<2_dp)
        res= res+(1_dp/real(fact(i),dp))
        print *,"Iteration:",i,"Value:",res
        i= i+1
        test= 1_dp/real(fact(i+1),dp)
      
     end do
end program Euler