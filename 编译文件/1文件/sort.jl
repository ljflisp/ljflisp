function linearsearch(haystack,needle)
   flag= false
   for i in 1:length(haystack)
    check= haystack[i]== needle
    if check
      flag= true
    end
    println("Index[$i] = haystack[$i] == $needle? ",check)
  end
  if flag
    println("\n $needle is in the collection. \n")
  else
    println("\n $needle is not in the collection. \n")
  end
  return flag
end

data = rand('a':2:'z',10)
println(data)
data = [data...,'g']
linearsearch(data,'e')
linearsearch(data,'g')
function guessinggame(lower= 0,upper= 100)
  attempts= 1
  guesslimit= round(Int,log(upper-lower)/log(2),RoundUp)
  println("\nThink of number between $lower and $upper")
  println("\n I will guess within $guesslimit")
  println("Press ENTER to continue")
  readline()

  while true
    guess = lower+round(Int,(upper-lower)/2,RoundDown) 
    if attempts > guesslimit
      break
    end
    print("I guess: $guess \n [L]Lower,[H]Higher or [C]Correct? ")
    input = readline()
    while input ∉ ["l","h","c","y"]
      print("Press enter L,H or C : ")
      input = readline()
    end
    if input=="h"
      upper = guess
    elseif input ==  "l"  
      lower = guess
    else
        break
    end
    attempts+= 1
 end

 if  attempts>guesslimit
      println("\n I give up.Did you forget your number?")
 elseif attempts== 1
     println("\nI win! It only took me 1 guess.")
  else
     println("\nI win! It took me $attempts guess.")
  end
end  
guessinggame(1,200)