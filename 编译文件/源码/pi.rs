const DIGITS :u32= 308;

fn main(){
  //print!("hello,again!")
  let mut d:u64 = 0u64;
  let  h:u64 = 1e9 as u64;
  let mut b:u32 = 30*((DIGITS+25)/9);
  let mut c:u32= b;
  let mut e:u32= 0;
  let mut f:Vec<u32>= vec![0;4*c as usize];
  while c>0{
    while b>0{
      d= d*(b as u64)+h*(if e!= 0 {f[b as usize]as u64}else{2});
      f[b as usize]= (d%((2*b-1)as u64))as u32;
      d /= (2*b-1)as u64;
      b-= 1;
    }
    if e!= 0{
      print!("{}",(e as u64)+d/h);}
      else{
      print!("{}.",(e as u64)+d/h);
    }
    e= (d%h)as u32;
    c-= 30;
    b= c;
  }
  print!("\n");
}