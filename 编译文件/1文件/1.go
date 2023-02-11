package main
import (
  "fmt"
  "bufio"
  "os"
  //"strconv"
)
func main(){
  //fmt.Println("hello,Go")
  input := bufio.NewScanner(os.Stdin)
  fmt.Printf("What is your favorite program language? ")
  input.Scan()
  name := input.Text()
  if(name=="swift"|| name==  "Swift"){
    fmt.Printf("Swift is awesome!")
  }else if(name=="python"|| name==  "Python"){
    fmt.Printf("Python is easy to use!")
  }else{
   // name := input.Text()
  //fmt.Printf("Hello,%q !\n",name)
    fmt.Printf("Hello , "+name+" !")
    //!不能省略不然就有"name"没有用
    //wssswissww
  }
}
