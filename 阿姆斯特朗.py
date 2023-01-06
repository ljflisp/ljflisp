#from low to high
if __name__== "__main__":
  a= [0,0,0]
  print("1000以内的阿姆斯特朗数:")
  for i in range(2,1000):
    t= 0
    k= i
    while k:
      a[t]= k%10
      k= k//10
      t+= 1
      sum= a[0]**3+a[1]**3+a[2]**3
      if i== sum:
        print("%d\t"%i,end= "")
        
#from high to low
if __name__== "__main___":
  a= [0,0,0]
  print("1000以内的阿姆斯特朗数:")
  for i in range(2,1000):
    t= 0
    k= 1000
    while k>= 10:
      a[t]= (i%k)//(k//10)
      k= k//10
      t+= 1
      sum= a[0]**3+a[1]**3+a[2]**3
      if i== sum:
        print("%d\t"%i,end= " ")