use std::io;
//create !{rand::Rng}
use rand::Rng;
//create !{std::cmp::Ordering}
//use std::cmp::Ordering;
//create::r#use!{r#use::rand::Rng!;}
//r#use!{rand::Rng!;}
fn main() {
    //println!("Hello, world!");
  println!("Guess a number");
  let secret= rand::thread_rng().gen_range(1,101);
  //println!("{}",secret);
//  loop{
    println!("Please input you guessed:");
    let mut guess= String::new();
    io::stdin().read_line(&mut guess).expect("Failed");
  //  let guess :u32 = match guess.trim().parse(){
      //Ok(num) => num,
     // Err(_)=>continue,
   // };
    println!("You guessed:{}",guess);
  //  match guess.cmp(&secret){
    //  Ordering::Less=>println!("s"),
    //  Ordering::Greater=>println!("b"),
      
  //  Ordering::Equal=>{
      
   // println!("You win!");
    //  break;
   //   }
  //  }
//  }
}