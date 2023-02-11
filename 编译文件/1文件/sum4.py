class Solution:
  def fourSum(self,nums,target):
    nums.sort()
    res=[]
    length= len(nums)
    for i in range(0,length-3):
      if i and nums[i] == nums[i-1]:
        continue
      for j in range(i+1,length-2):
        if j!= i+1 and nums[j]==nums[j-1]:
          continue
        sum= target-nums[i]-nums[j]
        left,right= j+1,length-1
        while left<right:
          if nums[left]+nums[right]==sum:
            res.append([nums[i],nums[j],nums[left],nums[right]])
            right-= 1
            left+= 1
            while left<right and nums[left]== nums[left-1]:
              left+= 1
            while left<right and nums[right]== nums[right+1]:
              right-= 1
          elif nums[left]+nums[right]>sum:
            right-= 1
          else:
            left+= 1
    return res          

if __name__== "__main__":
  s= Solution()
  List1 = [1,2,3,-6]
  nums1 = 0
  #print(s.fourSum(List1,nums1))

class Solution:
  def fourSumCount(self,A:list[int],B:list[int],C:list[int],D:list[int])->int:
    mapper= {}
    res= 0
    for i in A:
      for j in B:
        mapper[i+j]=mapper.get(i+j,0)+1
    for i in C:
      for j in D:
        res += mapper.get(1*(i+j),0)
      return res

if __name__== "__main__":
  s= Solution()
  A= [1,2]
  B= [-2,-1]
  C= [-1,2]
  D= [0,2]
  #print(s.fourSumCount(A,B,C,D))