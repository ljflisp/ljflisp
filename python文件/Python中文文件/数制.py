def char_to_num(ch):
  if ch>= '0'and ch<='9':
    return int(ch)
  else:
    return ord(ch)
    
def num_to_char(num):
  if num>= 0and num<= 9:
    return str(num)
  else:
    return chr(num)
    
def  source_to_decimal(temp,source):
  decimal_num= 0
  for i in range(len(temp)):
    decimal_num= (decimal_num*source)+char_to_num(temp[i])
  return decimal_num
  
def decimal_to_object(decimal_num,object):
  decimal= []
  while decimal_num:
    decimal.append(num_to_char(decimal_num%object))
    decimal_num//= object
  return decimal

def output(decimal):
  f= len(decimal)-1
  while f>= 0:
    print(decimal[f],end= "")
    f-= 1
  print()
if __name__== "__main__":
  MAXCHAR= 101
  flag= 1
  while flag:
    print("转换前的数是:",end= "")
    temp= input()
    print("转换前的数制是:",end= "")
    source= int(input())
    print("转换后的数制是:",end= "")
    object= int(input())
    print("转换后的数是:",end= "")
    decimal_num= source_to_decimal(temp,source)
    decimal= decimal_to_object(decimal_num,object)
    output(decimal)
    print("继续请输入1,否则输入0: ")
    flag=int(input())