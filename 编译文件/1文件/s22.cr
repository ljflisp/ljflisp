#puts "hello world"
str= "Lisp"

p! str.size
p! str + str
p! str * 3
p! str.upcase
p! str.downcase
p! str.starts_with?("Li")
p! str.ends_with?("sp")
p! str.includes?("is")
p! "is".in?(str)

len_sum= 0
strs = [] of String

loop do
  str= read_line
  break if str== "QUIT"#害人不浅== 
  strs.push str
  len_sum= len_sum+str.size
end

p! len_sum
p! strs

len_sum2= 0
strs.each do |s|
  len_sum2 = len_sum2 +s.size
end

p! len_sum2