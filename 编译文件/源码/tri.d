import std.stdio;

void pyra(int n) {
    int k= n+2;
    for(int i= 0;i<n;i++ ) {
      for(int j= 0;j<k;j++) {
        write(" ");
      }
      k-= 1;
      for(int j= 0;j<= i;j++){
        write(" ⬛ ");
      }
      writeln("");
    }
}

void main(string[] args) {
     int size;
     writeln("How big do you want the pyramid to be ?");
     readf("%d",&size);
     pyra(size);
}