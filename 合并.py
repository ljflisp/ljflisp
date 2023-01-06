class Solution:
    def mergeSortedArray(self,A,B):
         i,j= 0,0
         C= []
         while i<len(A) and j<len(B):
             if A[i]<B[j]:
                 C.append(A[i])
                 i+= 1
             else:
                 C.append(B[j])
                 j+= 1
         while i<len(A):
               C.append(A[i])
               i += 1
         while i<len(B):
               C.append(B[i])
               j+= 1
         return C
#主函数
if __name__== "__main__":
    A= [1,4]
    B= [1,2,3]  
    D= [1,2,3,4]
    E= [2,4,5,6]
    solution= Solution()
    print("输入:",A,"",B)
    print("输出:",solution.mergeSortedArray(A,B))
    print("输入:",D,"",E)
    print("输出:",solution.mergeSortedArray(D,E))
  
    