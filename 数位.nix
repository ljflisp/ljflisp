class Solution:
  def findNthDigit(self,n):
    length= 1
    count= 9
    start= 1
    while n>length*count:
      n-= length*count
      length+= 1
      count*= 10
      start*= 10
    start+= (n-1)//length
    return int(str(start)[(n-1)%length])

if __name__== "__main__":
  s= Solution()
  n= 11
  print("输入:",n)
  print("输出:",s.findNthDigit(n))