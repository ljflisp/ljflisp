\ echo "hello world"
: FIZZER DUP
   0 = IF
     ." FizzBuzz" CR
   ELSE
    DUP
    6 = IF
      ." Fizz" CR
    ELSE
      DUP
      10 = IF
        ." Buzz" CR
      ELSE
        ROT . CR
      THEN 
    THEN
  THEN
  DROP
;

: POW OVER SWAP  1 ?DO OVER * LOOP NIP ;
: FIZZBUZZ-LOOP 101 1 DO I I 4 POW 15 MOD FIZZER LOOP ;
FIZZBUZZ-LOOP