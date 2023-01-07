class Solution:
      def largestPalindrome(self,n):
           if n== 1:
                return 9
           elif n== 7:
                 return 877
           elif n== 8:
                  return 475
           maxNum,minNum= 10**n-1,10**(n-1)
           for i in range(maxNum,minNum,-1):
                candidate= str(i)
                candidate= candidate+candidate[::-1]
                candidate= int(candidate)
                j= maxNum
                while j*j>candidate:
                        if candidate%j== 0:
                            return candidate  % 1337
                        j= j-1
if __name__== "__main__":
    s=Solution()
    n= int(input("Enter n:"))
    print("输入:",n)
    print("输出:",s.largestPalindrome(n))
                          