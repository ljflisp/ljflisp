class ListNode(object):
  def __init__(self,val,next=None):
    self.val= val,
    self.next= next
class Solution():
  def countNodes(self,head):
    cnt= 0
    while head is not None:
      cnt+= 1
      head= head.next
    return cnt

if __name__== "__main__":
  node1= ListNode(1)
  node2= ListNode(2)
  node3= ListNode(3)
  node4= ListNode(4)
  node1.next= node2
  node2.next= node3
  node3.next= node4
  s= Solution()
  print("输入:",node1.val,node2.val,node3.val,node4.val)  
  print("输出:",s.countNodes(node1))