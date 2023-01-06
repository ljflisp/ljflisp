if __name__== "__main__":
  n= int(input("请输入所选范围上限: "))
  i= 2
  while i<= (n//2):
    s= 0
    j= 1
    for j in range(i):
      if j!=0 and i%j== 0:
        s+= j
      j+= 1
      if s== i:
        print("2到%d之间的完数: %d"%(n,i))
    i+= 1
    