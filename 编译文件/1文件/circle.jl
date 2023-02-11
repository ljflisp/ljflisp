struct Circle
  radius :: Float64
end

function perimeter(c::Circle)
  2 * π * c.radius
end

function area(c::Circle)
  π * c.radius^2
end

c = Circle(3.0)

print("园的周长: ")
println(perimeter(c))
print("园的面积: ")
println(area(c))