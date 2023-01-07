if __name__== "__main__":
  flag= 0
  i= 23
  while flag== 0:
   j= 1
   x= i
   while j<=4 and x>= 11:
      if(x+1)%(j+1)== 0:
        x-= (x+1)//(j+1)
      else:
        x= 0
        break
      j+= 1
    if j== 5 and x== 11:
      print("原来鱼缸中共有%d条金鱼."%i)
      flag= 1
       i+= 2
        
    

