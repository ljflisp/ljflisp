class Solution:
  def hmpathsum(self,nums):
    return sum(b.count('0')*b.count('1')for b in zip(*map('{:032b}'.format,nums)))
    
    """其实就是汉明路径的不同数位的和"""    
    
if __name__== "__main__":
  s= Solution()
  n= [4,14,2]
  #4= 0010 14= 1110 2= 0010
  print("输入:",n)
  print("输出:",s.hmpathsum(n))