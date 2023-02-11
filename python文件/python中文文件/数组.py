class Solution:
       def checkPossibility(self,nums):
           count= 0
           for i in range(1,len(nums)):
                  if nums[i]<nums[i-1]:
                        count+= 1
                        if i>= 2 and nums[i]<nums[i-2]:
                             nums[i]=nums[i-1]
                        else:
                            nums[i-1]= nums[i]
           return count<=1   
         
if __name__==  "__main__":
      solution= Solution()
      nums=[4,2,3]
      print("输入:",nums)
      print("输出:",solution.checkPossibility(nums))