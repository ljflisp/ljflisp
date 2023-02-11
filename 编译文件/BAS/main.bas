DECLARE FUNCTION Factorial (n)
FUNCTION Factorial (n) 
    IF n= 0 THEN 
      Factorial = 1
    ELSE
      Factorial = n*Factorial(n-1)
    END IF
  END FUNCTION 
  PRINT "6! = ";Factorial(6)
  
  INPUT NAME$
  PRINT "Hello,";NAME$;"!"
  
FOR  i% = 1 TO 20
  PRINT STRING$(i%,"*")
NEXT i%