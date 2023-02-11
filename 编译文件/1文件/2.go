package main
import(
  "fmt"
)
type ljflisp struct {
  pi float64
  a float64
  s float64
}
func (this *ljflisp) iterate() float64 {
   s := this.s
   a := this.a
   //p := this.p
  this.pi += s*(4/(a*(a*(a+3)+2)))
  this.a += 2
  this.s = -s
  return this.pi
}

func main(){
  pai := ljflisp{3,2,1}
  for i:= 0;i<150000;i++{
    pai.iterate()
  }
  fmt.Println("pi= ",pai.pi)
}