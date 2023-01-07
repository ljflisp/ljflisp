class Solution:
  def getCombination(self,n,k):
    C= [[0]*(n+1)for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,i):
          C[i][j]= C[i-1][j-1]+C[i-1][j]
        ans= []
        curr_index= 1
        for i in range(1,n//2+1):
          base= C[n-curr_index][n//2-i]
          while k<base:
            curr_index=curr_index+1
            base=base+C[n-curr_index][n//2-i]
            base=base- C[n-curr_index][n//2-i]
            k= k-base
            ans.append(curr_index)
            curr_index+= 1
        return ans

if __name__== "__main__":
  s= Solution()
  a= 8
  k= 11
  print("人数:",a,"找第k组:",k)
  print("第k组:",s.getCombination(a,k))