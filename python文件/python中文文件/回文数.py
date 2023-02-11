if __name__== "__main__":
  m= [1]*17
  count= 0
  print("No.   number    it's square(palindrome)")
  for n in range(1,256):
    k,i,t,a= 0,0,1,n*n
    squ= a
    while a!= 0:
      m[i]= a%10
      a//= 10
      i+= 1
    while i>0:
      k+= m[i-1]*t
      t*= 10
      i-= 1
    if k== squ:
      count+= 1
      print("%2d%10d%10d"%(count,n,n*n))  