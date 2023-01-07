#对称二叉树
class TreeNode:
  def __init__(self,val):
    self.val= val
    self.left= None
    self.right= None

class Solution:
  def help(self,p,q):
    if p== None and q== None:return True
    if p and q and p.val== q.val:
      return self.help(p.right,q.left)and self.help(p.left,q.right)
    return False
  def isSymmetric(self,root):
      if root:
        return self.help(root.left,root.right)
        return True

if __name__== "__main__":
  root= TreeNode(1)
  root.left= TreeNode(2)
  root.right= TreeNode(2)
  root.right.right= TreeNode(3)
  root.right.left= TreeNode(4)
  root.left.right= TreeNode(4)
  root.left.left= TreeNode(3)
  solution= Solution()
  print("输入:",root.val,root.left.val,root.right.val,root.left.left.val,root.left.right.val,root.right.left.val,root.right.right.val)
  print("输出:",solution.isSymmetric(root))