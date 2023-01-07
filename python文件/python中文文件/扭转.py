class TreeNode:
  def __init__(self,val):
    self.val= val
    self.left= None
    self.right= None
    
class Solution:
  def isTweakedIdentical(self,a,b):
    if a== None and b== None:return True
    if a and b and a.val== b.val:
       return self.isTweakedIdentical(a.left,b.left)and\
              self.isTweakedIdentical(a.right,b.right)or\
      self.isTweakedIdentical(a.left,b.right)and\
      self.isTweakedIdentical(a.right,b.left)
    return False
if __name__== "__main__":
  root= TreeNode(1)
  root.left= TreeNode(2)
  root.right= TreeNode(3)
  root.left.left= TreeNode(4)
  
  root1= TreeNode(1)
  root1.right= TreeNode(2)
  root1.left= TreeNode(3)
  root1.right.right= TreeNode(4)
  s=Solution()
  print("输入:",root.val,root.left.val,root.right.val,root.left.left.val,",",root1.val,root1.left.val,root1.right.val,root1.right.right.val)
  print("输出:",s.isTweakedIdentical(root,root1))