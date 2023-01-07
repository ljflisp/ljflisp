class Solution:
   def flatten(self,nestedList):
       stack= [nestedList]
       flatten_list= []
       while stack:
         top= stack.pop()
         if isinstance(top,list):
           for elem in reversed(top):
             stack.append(elem)
         else:
           flatten_list.append(top)
       return flatten_list

if __name__== "__main__":
  s= Solution()
  nums= [1,[2,[3,4,[5,6]]]]
  flatten_list= s.flatten(nums)
  print("输入:",nums)
  print("输出:",flatten_list)