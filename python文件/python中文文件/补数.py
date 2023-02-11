class Solution:
      def findComplement(self,num):
          return num^((1<<num.bit_length())-1)
if __name__==  "__main__":
    s= Solution()
    n= 15
    print("输入:",n)
    print("输出:",s.findComplement(n))