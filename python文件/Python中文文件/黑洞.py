def three_max(a,b,c):
  if a<b:
    t= a
    a= b
    b= t
  if a<c:
    t= a
    a= c
    c= t
  if b<c:
    t= b
    b= c
    c= t
  return a*100+b*10+c

def three_min(a,b,c):
  if a<b:
    t= a
    a= b
    b= t
  if a<c:
    t= a
    a= c
    c= t
  if b<c:
    t= b
    b= c
    c= t
  return c*100+10*b+a
def black_number(max,min):
  j= max-min
  k= 0
  while k<min:
    h= j
    hun=j//100
    ten= j%100//10
    bit= j%10
    max= three_max(hun,ten,bit)
    min= three_min(hun,ten,bit)
    j= max-min
    if j== h:
      print("%d"%j)
      break
    k+= 1
if __name__== "__main__":
  i=int(input("请输入一个3位整数: "))
  hun= i//100
  ten= i%100//10
  bit= i%10
  max= three_max(hun,ten,bit)
  min= three_min(hun,ten,bit)
  print("max= ",max)
  print("min= ",min)
  black_number(max,min)  