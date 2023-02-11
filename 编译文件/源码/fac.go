package main

import "fmt"

var fac int

func facm ( facn int) int {
  fac = 1
  for i:= 1;i<= facn;i++{
    fac = fac * i
  }
  return fac
}
func main(){
  fmt.Println(facm(5))
}