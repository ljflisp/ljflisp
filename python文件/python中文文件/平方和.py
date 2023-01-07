import math
class Solution:
  '''
  参数num:整数
  返回布尔类型
  '''
  def checksumOfSquareNumbers(self,num):
    #write your code here
      if num<0:
        return False
      for i in reversed(range(0,int(math.sqrt(num))+1)):
        if i*i== num:
          return True
        j= num-i*i
        k= int(math.sqrt(j))
        if k*k== j:
          return True
      return False

if __name__== "__main__":
  s= Solution()
  num=int(input("请输入:"))
  print("输出:",s.checksumOfSquareNumbers(num))
      