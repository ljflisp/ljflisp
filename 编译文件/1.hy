(defn fac [n]
  (if (=  n 1)
      1
      (* n (fac (- n 1)))  ) )
(print (fac 5))

(defn fib [n]
     (if (=  n 1) 
        1
     (if (=  n  2) 
        1
     (+ (fib (- n 1)) (fib (- n 2)) )   )   )  )
(print (fib 10))

(defn f [x y]
    (+ (* x y) y )   )
(print (f 3 4))


(defn sgn [x] 
       (cond   [(<=  x 0) -1]          
               [(> x 0)  1]
       )  
)

(print (sgn 0))
(print (sgn 1))
(print (sgn -3))