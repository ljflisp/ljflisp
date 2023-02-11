package main

import (
  "fmt"
  //"math"
)

func fib(n uint) uint {
  if n== 0 {
    return 0
  }else if n== 1 {
    return 1
  }else{
    return fib(n-1)+fib(n-2)
  }
}


func main() {
  i := uint(0)
  for(i<20){
    fmt.Println(fib(i))
    i += 1
  }
  fmt.Println(fib(30))
  fmt.Println("Process finished.")
}