if __name__== "__main__":
  last= 1
  print("请输入两个数x和y: ")
  x= int(input("x= "))
  y= int(input("y= "))
  for i in range(1,y+1):
    last= last*x%1000
    print("%d的%d次方所得积的后3位为: %d"%(x,y,last))