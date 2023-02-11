if __name__== "__main__":
  a= [-3,4,7,9,13,45,67,89,100,180]
  k= -1
  print("A array:")
  for i in a:
    print(i,end= " ")
  print()
  m=int(input("Enter m =:"))
  i= 0
  while i<len(a):
    if m== a[i]:
       k= i
       break
    i+= 1
if k>= 0:
  print("m= %d,index= %d"%(m,k))
else:
  print("Not be found!")       