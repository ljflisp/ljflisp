if __name__== "__main__":
  print("result is:")
  for n in range(100,1000):
    hun= n//100
    ten= (n-hun*100)//10
    ind= n%10
    m= hun**3+ten**3+ind**3
    if n== m:
       print("%d\t"%n,end="")