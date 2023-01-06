if __name__== "__main__":
  a= [-3,4,7,9,13,45,67,89,100,180]
  low= 0
  high= len(a)-1
  k= -1
  print("A array:")
  for i in a:
    print(i,end= " ")
  print()
  m= int(input("Enter m =:"))
  while low<= high:
    mid= (low+high)//2
    if m<a[mid]:
      high= mid-1
    else:
      if m>a[mid]:
        low= mid+1
      else:
        k= mid
        break
if k>= 0:
  print("m= %d,index= %d"%(m,k))
else:
  print("Not be found!")