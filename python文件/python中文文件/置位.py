class Solution(object):
  def countPrimeSetBits(self,L,R):
    k= 0
    for n in range(L,R+1):
      if bin(n).count('1') in[2,3,5,7,11,13,17,19]:
           k=k+1
    return k

if __name__== "__main__":
  s= Solution()
  L= 6
  R= 10
  print("输入:[",L,R,"]")
  print(s.countPrimeSetBits(L,R))