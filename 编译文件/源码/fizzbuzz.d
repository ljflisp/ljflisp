import std.stdio;

void main(string []args) {
  for(int i= 0;i< 100+1;i++) {
    if(i%3== 0 && i%5== 0) {
      writefln("FizzBuzz");
    }else if(i%3== 0 && i%5!= 0){
      writefln("Fizz");
    }else if(i%3!= 0 && i%5== 0) {
      writeln("Buzz");
    }else{
      writeln(i);
    }
  }
}