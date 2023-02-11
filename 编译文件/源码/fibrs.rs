fn fib(n: i64) -> i64 {
  if n == 0 {
    return 0;
  }else if n<= 2{
    return 1;
  }else{
    return fib(n-1)+fib(n-2);
  }
}

fn main() {
  let mut i= 1;
  while i<11 {
    println!("{}",fib(i));
    i+= 1;
  }
  println!("{}",fib(11));
}