class listNode(object):
  def __init__(self,val):
    self.val= val
    self.next= None
    
    
class Solution:
  def addLists(self,l1,l2)->list:
    dummy= listNode(None)
    tail=dummy
    carry= 0
    while l1 or l2 or dummy:
      num= 0
      if l1:
        num+= l1.val
        l1= l1.next
      if l2:
        num+= l2.val
        l2= l2.next
      num+=carry
      digit,carry=num%10,num//10
      node= listNode(digit)
      tail.next,tail=node,node
    return dummy.next
if __name__== "__main__":
  s= Solution()
  l0= listNode(7)
  l1= listNode(1)
  l2= listNode(6)
  l0.next= l1
  l1.next= l2
  l3= listNode(5)
  l4= listNode(9)
  l5= listNode(2)
  l3.next= l5
  l4.next= l5    
  ans= s.addLists(l0,l3)  
  a=[ans.val,ans.next.val,ans.next.next.val]  
  print("输入:7->1->6->null,5->9->2->null")
  print("输出:2->1->9->null")