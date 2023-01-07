if __name__== "__main__":
  print("请输入一个正整数n: ",end= "")
  n= int(input())
  if n<= 0:
    print("输入错误")
    exit()
  count= 0
  while n!= 0:
    n= n//10
    count+= 1
  print("%d位数"%count)