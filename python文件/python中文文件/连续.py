class Solution:
      def countSegment(self,s):
           res= 0
           for i in range(len(s)):
               if  s[i]!= ''and(i== 0 or s[i-1]== ''):
                      res+= 1
           return res
if __name__== "__main__":   
 s= Solution()
 n= "Hello,my name is John"
print("输入:",n)
print("输出:",s.countSegment(n))