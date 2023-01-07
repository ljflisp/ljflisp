if __name__== "__main__":
  i= 0
  money= 0.0
  while i<5:
    money= (money+1000)/(1+0.0063*12)
    i+= 1
print("应该存入钱数为: %0.2f"%money)