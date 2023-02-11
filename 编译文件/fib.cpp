#include <iostream>
using namespace std;
int main(){
  int n1= 0;
  int n2= 1;
  int count = 0;
  cout<< "How many fib number do you want ?\n";
  int e;
  cin>>e;
  if(e<= 1){
    print(1);
  }else{
    while(count<e){
      cout<<e<<"\n";
      int nth = n1 + n2;
      n1 = n2;
      n2 = nth;
      count+= 1;
    }
  }
}