class Solution:
  #nums:整数数组
  #k:滑动窗口大小
  #返回:每个窗口的数字和
  def winSum(self,nums,k):
    n= len(nums)
    if n<k or k<= 0:
      return []
    sums= [0]*(n-k+1)
    for i in range(k):
      sums[0]+= nums[i]
    for i in range(1,n-k+1):
      sums[i]= sums[i-1]-nums[i-1]+nums[i+k-1]
    return sums

if __name__== "__main__":
  s= Solution()
  int_nums= [1,2,7,8,5]
  k= 3
  print("输入数组:",int_nums)
  print("输入窗口:",k)
  print("输出数组:",s.winSum(int_nums,k))