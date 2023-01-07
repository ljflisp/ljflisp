if __name__== "__main__":
   print("请输入100000以内的自守数: ")
   for number in range(0,100000):
     mul= number
     k= 1
     while (mul//10)>0:
       mul//= 10
       k*= 10
       a=k*10
       mul= 0
       b= 10
       while k>0:
         mul= (mul+(number%(k*10))*(number%b-number%(b//10)))%a
         k//= 10
         b*=10
       if number==mul:
         print("%ld"%number,end= " ")