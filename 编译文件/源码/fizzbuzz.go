package main

import (
  "fmt"
  "math"
)

func main(){
  for n := 1; n<= 100; n++ {
    switch  (int(math.Pow(float64(n),  4.0))%15) {
          case 0:
                fmt.Printf("FizzBuzz\n");
      break;
          case 1:
      fmt.Printf("%d\n",n)
          case 6:
      fmt.Printf("Fizz\n")
      break;
          case 10:
      fmt.Printf("Buzz\n")
      break;      
    }
  }
}