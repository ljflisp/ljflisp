from itertools import permutations #s I hate you
def board(vec):
  for col in vec:
    s = ['-'] * len(vec)
    s[col]= "Q"
    print("  "+'  '.join(s))
    print()

n= 8
solution_number= 0
cols= range(n)
for vec in permutations(cols):
  if (n== len(set(vec[i]+i for i in cols))
       == len(set(vec[i]-i for i in cols))):
       solution_number+= 1 
        
      # while   (solution_number==2):
       print(solution_number)
       board(vec)#hate board
       if(solution_number== 2):
         break