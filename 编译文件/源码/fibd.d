import std.stdio;

int fib(int n){
  if(n == 0){
    return 0;
  }else if(n<= 2){
    return 1;
  }
  return fib(n-1)+fib(n-2);
}
void main(string[] args){
  //int i;
  for(int i= 0;i<10;i++){
    writeln(fib(i));
  }
  writeln(fib(10));
}