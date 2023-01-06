if __name__== "__main__":
  print("\t红球 \t白球 \t黑球")
  print(".......................")
  num= 0
  for m in range(0,4):
    for n in range(0,4):
      if 8-m-n<= 6:
        num+= 1
        print("%2d:%d\t\t%d\t\t%d"%(num,m,n,8-m-n))
  