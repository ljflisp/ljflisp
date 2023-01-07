class TrieNode:
  def __init__(self):
    self.children= {}
    self.is_word= False
class WordDictionary:
  def __init__(self):
    self.root= TrieNode()
  def addWord(self,word):
    node= self.root
    for c in word:
      if c not in node.children:
        node.children[c]=TrieNode()
        node= node.children[c]
        node.is_word= True
  def search(self,word):
    if word is None:
      return False
    return self.search_helper(self.root,word,0)
  def search_helper(self,node,word,index):
    if node is None:
      return False
    if index>=len(word):
      return node.is_word
    char= word[index]
    if char != '.':
        return self.search_helper(node.children.get(char),word,index+1)
    for child in node.children:
      if self.search_helper(node.children[child],word,index+1):
        return True
    return False
if __name__== "__main__":
  solution= WordDictionary()
  solution.addWord("bad")
  solution.addWord("dad")
  solution.addWord("mad")
  print('输入:addWord("bad"),addWord("dad"),addWord("mad")')
  print('输入:search("pad"),search(dad),search(".ad"),search("b..")')
  print("输出:",
       solution.search("pad"),
       solution.search("bad"),
       solution.search(".ad"),
       solution.search("b..")) 
      