if __name__== "__main__":
  x= int(input("请输入一个5位数整数:"))
  if x<10000or x>99999:
    print("输入错误")
  else:
    ten_thousand= x//10000
    thousand= x%10000//1000
    ten= x%100//10
    indiv= x%10
    if indiv== ten_thousand and ten==  thousand:
      print("%d是回文数"%x)
    else:
      print("%d不是回文数"%x)
    