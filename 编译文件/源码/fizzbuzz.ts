//console.log("helloworld")
//var i :number = 1;
for(i= 1;i<100+1;i++) {
  if(i%3== 0 && i%5== 0){
    console.log("FizzBuzz");
  }else if(i%3!= 0 && i%5== 0){
    console.log("Fizz");
  }else if(i%3== 0 && i%5!= 0){
    console.log("Buzz");
  }else{
    console.log(i);
  }
}