function fib(n1= 0,n2= 1,count= 0,nth= 11) {
  if(nth<= 0){
    count+= 1;
    console.log("Please enter nth>=0")
  }else if(nth<= 2){
    return 1;
  }else{
     while(count<nth){
       console.log(n1);
       let nth= n1+n2;
       n1= n2;
       n2= nth;
       count+= 1;       
     }
  }
}
console.log(fib());