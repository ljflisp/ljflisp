bigfib = go 2 1 1 where  
    go i a b
        | length (show b) >= 1000  = (i,b)
        | otherwise  = go (i+1) b (a+b)
 
selfpowers = slice $ show $ sum[i ^ i | i <- [1..1000]]  where 
   slice s = drop(length s -10) s

main= do
   print bigfib
   putStr "\n"
   putStr selfpowers