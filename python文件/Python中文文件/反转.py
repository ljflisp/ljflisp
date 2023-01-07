class Solution:
     def reverseInteger(self,number):
       h= int(number/100)
       t= int(number%100/10)
       z= int(number%10)
       return(100*z+10*t+h)
if __name__==  "__main__":
    solution= Solution()
    num= 123
    ans= solution.reverseInteger(num)
    print("输入:",num)
    print("输出:",ans)