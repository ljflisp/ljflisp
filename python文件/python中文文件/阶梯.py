import math
class  Solution:
  def arrangeCoins(self,n):
    return math.floor((-1+math.sqrt(1+8*n))/2)

if __name__== "__main__":
  n= 10
  s= Solution()
  print("输入:",n)
  print("输出:",s.arrangeCoins(n))