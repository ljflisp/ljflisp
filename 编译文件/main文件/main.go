package main 
import (
  "fmt"
  "bufio"
  "os"
  "strconv"
  "math/rand"
  "time"
)

func main() {
 // fmt.Println("helloworld")
  s1 := rand.NewSource(time.Now().UnixNano())
  r1 := rand.New(s1)
  scanner := bufio.NewScanner(os.Stdin)
  var secret int64= (r1.Int63()+1)%100
  for true{
    fmt.Println("Liar Test1")
    fmt.Println("Please guess a number between 0 and 100 (word small= actual big,word big= actual small): ")
    scanner.Scan()
    in, _ := strconv.ParseInt(scanner.Text(),10,64)
    if(in > secret){
      fmt.Println("Sorry,too small!")
    }else if(in < secret){
      fmt.Println("Sorry,too big!")
    }else{
      break
    }  
   //我去,这里不能省略了(省略了就永远不能break) 不是这里的原因写反了
  }
  fmt.Println("Correct!")
}