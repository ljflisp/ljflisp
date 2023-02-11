class Solution:
      def canConstruct(self,ransomNote,magazine):
          arr= [0]*26
          for c in magazine:
               arr[ord(c)-ord('a')]+= 1
          for c in ransomNote:
               arr[ord(c)-ord('a')]-= 1
               if arr[ord(c)-ord('a')]:
                   return False
          return True
if __name__== "__main__":        
    s= Solution()       
    ransomNote= "aa"                  
    magazine= "aab"                  
    print("输入勒索信:",ransomNote)                      
    print("输入杂志内容:",magazine)   
    print("输出:",s.canConstruct(ransomNote,magazine))