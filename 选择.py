def sle(a):
  n= len(a)
  for i in range(0,n-1):
    for j in range(i+1,n):
      if a[j]<a[i]:
        t= a[i]
        a[i]= a[j]
        a[j]= t
  for i in a:
   print(a,end= " ")
if __name__== "__main__":
  print("赋初值:")
  x= input()
  a= x.split(" ")
  for i in range(0,len(a)):
    a[i]= int(a[i])
    print("Enter below:\n",a)
    print("After converting,it is:")
  sle(a)