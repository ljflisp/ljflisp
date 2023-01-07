class Solution:
      def longestWord(self,words):
           words.sort()
           words.sort(key= len,reverse= True)
           res= []
           for word in words:
               temp= word
               i= 1
               for i in range(len(temp)):
                     if temp[:len(temp)-i] in words:
                          if i== len(temp)-1:
                               return temp
                          continue 
                     else:
                         break
           return ''
if __name__==  '__main__':
   s= Solution()
   words= ["w","wo","wor","worl","world"]
   print("输入字典:",words)
   print("输出单词:",s.longestWord(words))
