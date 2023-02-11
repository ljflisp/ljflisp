fn main(){
  //println!("helloworld");
  println!("{:#?}",
    (0..100).map(|n :usize| 
    match n.pow(4) % 15 {
      1 => n.to_string(),
      6 => "Fizz".to_string(),
      10 => "Buzz".to_string(),
      0 => "FizzBuzz".to_string(),
      _ => unreachable!()
    }).collect::<Vec<String>>());
}