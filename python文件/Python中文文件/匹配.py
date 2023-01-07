class Solution:
       def repeatedStringMatch(self,A,B):
             C= ""
             for i in range(int(len(B)/len(A)+3)):
                  if B in C:
                       return i
                  C+= A
             return -1
if __name__==  "__main__":
   s=Solution() 
   A= "abcd"
   B= "cdabcdab"
   print("输入字符串A:",A)
   print("输入字符串B:",B)
   print("需要重复次数:",s.repeatedStringMatch(A,B))
