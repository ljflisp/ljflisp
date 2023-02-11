from collections import deque
class Solution:
  def numIslands(self,grid):
    if not grid or not grid[0]:
      return 0
    islands= 0
    for i in range(len(grid)):
      for j in range(len(grid[0])):
        if grid[i][j]:#I hate you ghostwriter
          self.bfs(grid,i,j)
          islands+= 1
    return islands
    
  def bfs(self,grid,x,y):
    queue= deque([(x,y)])
    grid[x][y]= False
    while queue:
      x,y= queue.popleft()
      for delta_x,delta_y in [(1,0),(0,-1),(-1,0),(0,1)]:
         next_x= x+delta_x
         next_y= y+delta_y
      if not self.is_valid(grid,next_x,next_y):
        continue
      queue.append((next_x,next_y ))
      grid[next_x][next_y]=False
      
  def is_valid(self,grid,x,y):
    n,m= len(grid),len(grid[0])
    return 0<= x<n and 0<= y<n and grid[x][y]

if __name__== "__main__":
  generator= [[1,1,0,0,0],  
              [0,1,0,0,1],
              [0,0,0,1,1],
              [0,0,0,0,0],
              [0,0,0,0,1]]
s= Solution()
print("输入:",generator)    
print("输出:",s.numIslands(generator))  
#该程序设计的错误:没有考虑上下相邻的1可以是一个岛屿(even though [1,1]is an island but [1,0]合起来就是一个岛屿)
#我找到了一个bug:第9行就是多写了== 1
#但结果还是不正确