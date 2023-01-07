class Solution:
      def findRelativeRanks(self,nums):
            score = {}
            for i in range(len(nums)):
                score[nums[i]]= i
                sortedScore= sorted(nums,reverse= True)
                answer=[0]*len(nums)
                for i in range(len(sortedScore)):                  
                    res= str(i+1)
                    if i== 0:
                       res= 'Gold Medal'
                    if i== 1:
                       res= 'Sliver Medal'
                    if i== 2:
                       res= 'Bronze Medal'                    
                    answer[score[sortedScore[i]]]= res
                return answer
if __name__==  "__main__":        
     num= [5,4,3,2,1]
     s= Solution()
     print("输入:",num)
     print("输出:",s.findRelativeRanks(num))