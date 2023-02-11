abstract type Operator end

expression = Union{Operator,Integer}

struct Add <: Operator
  a :: expression
  b :: expression
end

struct Mul <: Operator
  a :: expression
  b :: expression
end
struct Sq <: Operator
  x :: expression
end

evaluate(x :: Integer) = x
evaluate(x :: Add)= evaluate(x.a)+evaluate(x.b)
evaluate(x :: Mul)= evaluate(x.a)*evaluate(x.b)

function evaluate(x :: Sq)
  y= evaluate(x.x)
  y*y
end

formula = Mul(Sq(2),Add(3,4))
println(evaluate(formula))