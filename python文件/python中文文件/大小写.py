class Solution(object):
  def letterCasePermutation(self,S):
    res= []
    indices= []
    indices= [i for i,_ in enumerate(S)if S[i].isalpha()]
    for i in range(0,pow(2,len(indices))):
      if i== 0:
        res.append(S)
      else:
        j= i;bpos= 0;nsl= list(S)
        while j>0:
          ci2c= indices[bpos]
          if j&1 and S[ci2c].islower():
            nsl[ci2c]= S[ci2c].upper()
          elif j&1and S[ci2c].isupper():
            nsl[ci2c]= S[ci2c].lower()
          bpos+= 1
          j= j>>1
          res.append("".join(nsl))
    return res

if __name__== "__main__":
  s= Solution()
  S= "a1b2"
  print("输入:",S)
  print("输出:",s.letterCasePermutation(S))    