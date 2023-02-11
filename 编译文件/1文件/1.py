import datetime
x=datetime.datetime.now()
#print(x)
class Solution:
  def spiralOrder(self,matrix):
    if matrix== []:
      return[]
      up= 0
      left= 0
      down= len(matrix)-1
      right= len(matrix[0])-1
      direct= 0
      res= []
      while True:
        if direct== 0:
          for i in range(left,right+1):
            res.append(matrix[up][i])
          up+= 1
        if direct== 1:
          for i in range(up,down+1):
            res.append(matrix[i][right])
          right-= 1
          if direct== 2:
            for i in range(right,left-1,-1):
              res.append(matrix[down][i])
            down-= 1
          if direct== 3:
            for i in range(down,up-1,-1):
              res.append(matrix[i][left])
            left+= 1
          if up>down or left>right:
            return res
          direct= (direct+1)%4
          
if __name__== "__main__":
  arr= [[1,2,3],[4,5,6],[7,8,9]]
  s= Solution()
 # print(arr)
  #print("Spiral matrices:",s.spiralOrder(arr))    #None 
  
#No.1
if __name__== "__main__":
  flog= 0
  for i in range(10):
     if flog:
        break
     for j in range(10):
       if flog:
         break
       if i!= j:
         k= 1000*i+100*i+10*j+j
         for temp in range(31,100):
           if temp*temp== k:
             #print(k)
             flog= 1
             break
#No.2
f= [1,1]                         
for i in range(2,365):
  n= f[i-1]+f[i-2]
  f.append(n)
#print(n)#第365位斐波拉契数列

# s -> t
class Solution:
  def twoSum(self,nums:list[int],target:int) -> list[int]:
    n = len(nums)
    mapper= {}
    for i in range(n):
      if (target-nums[i] in mapper):
        return [mapper[target-nums[i]],i]
      else:
         mapper[nums[i]]= i
    return []

if __name__== "__main__":
  s= Solution()
  nums= [9,8,7,6,2,1,3]
  target= 17
  #print(s.twoSum(nums,target))
for x in range(0,10000):
  if(x%2== 1 and x%5== 2 and x%7==  3 and x%9== 4):
    # print(x)