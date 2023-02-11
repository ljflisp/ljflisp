class Solution:
  def threeSum(self,nums:list[int]) -> list[list[int]]:
    n = len(nums)
    nums.sort()
    res= []

    for i in range(n-2):
      if  i > 0 and nums[i]==nums[i-1]:
        continue
      l= i+1
      r= n-1
      while(l<r):
        if(nums[i]+nums[l]+nums[r]<0):
         l += 1
        elif(nums[i]+nums[l]+nums[r]>0):
         r -= 1
        else:
            res.append([nums[i],nums[l],nums[r]])
            while(l<r and nums[l] == nums[l+1]):
               l+= 1
            while(l<r and nums[r] == nums[r-1] ):
               r-= 1
            l+= 1
            r-= 1
    return res   

if __name__== "__main__":
  s= Solution()
  nums= [1, 2, 3 , 4 ,-4 ,-5, -7]
  print(s.threeSum(nums))