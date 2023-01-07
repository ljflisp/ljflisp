class Solution:
  def topKFrequentWords(self,words,k):
    dict={}
    res= []
    for word in words:
      if word not in dict:
        dict[word]= 1
      else:
        dict[word]+=1
    sorted_d= sorted(dict.items(),key=lambda x:x[1],reverse=True)
    for i in range(k):
      res.append(sorted_d[i][0])
    return res
if __name__== "__main__":
  generator= ["yes","long","code",
             "yes","code","baby",
             "you","baby","chrome",
           "safari","long","code",
             "body","long","code"]
  k= 4
  solution= Solution()
  print("输入:",generator)
  print("输入:","k= ",k)
  print("输出:",solution.topKFrequentWords(generator,k))