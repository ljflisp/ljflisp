def bubble(a):
  n= len(a)
  i= 1
  while i<= n-1:
    j= 0
    while j< n-i:
      if a[j]>a[j+1]:
        t= a[j]
        a[j]= a[j+1]
        a[j+1]= t
      j+= 1
    i+= 1
  for a1 in a:
    print(a1,end= " ")

if __name__== "__main__":
   print("请为列表元素赋初值,列表末尾不能有空格:")
   x= input()
   a= x.split(" ")
   for i in range(0,len(a)):
     a[i]= int(a[i])
     print("您输入的列表元素为: \n",a)
     print("经过交换后的数组元素为: ")
   bubble(a)