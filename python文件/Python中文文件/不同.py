class Solution:
  def findtheDifferent(self,s,t):
      flag= 0
      for i in range(len(s)):
        flag+= (ord(t[i])-ord(s[i]))
      flag+=ord(t[-1])#there is -1，otherwise i-1,the output will be wrong(c)
      return chr(flag)#if you input flag without the blacket and chr it will be 99.

if __name__== "__main__":
  s= Solution()
  n= "abcd"
  t= "abcde"
  print("输入字符串1:",n)
  print("输入字符串2:",t)
  print("输出插入字符:",s.findtheDifferent(n,t))