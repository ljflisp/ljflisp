use std::io;
use rand::Rng;
use std::cmp::Ordering;

fn main() {
  //println!("helloworld");
  //println!("I love Rust!");
  //println!("Guess a number");
  let secret= rand::thread_rng().gen_range(1,101);
  println!("{}",secret);
  loop{
  println!("Please input the number:");
  let mut guess = String::new();
  io::stdin().read_line(&mut guess).expect("Failed to read line !");
  let guess:u32= guess.trim().parse().{
    Ok(num)=>num ,
    err(_)=>continue,
  };
    //O.expect("Please type a number!")
  println!("Your guessed:{}",guess);
  match guess.cmp( &secret) {
    Ordering::Less =>println!("Too small!");
    Orderibg::Greater =>println!("Too big!");
    Ordering::Equal => {
      println!("You win!");
        break;      
   }
}
 }
}