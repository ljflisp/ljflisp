var n1 = 0
var n2 = 1
var count = 0
print("How many Fibonacci Number do you want ?")
let amount = readLine()
if let fib_number = Int(amount!) {
  if fib_number <= 0 {
    print("Please enter a valid number")
  } else if fib_number <= 1 {
    print(1)
  } else {
    while count < fib_number {
      var nth = 0
      print(n1)
      nth = n1 + n2
      n1 = n2
      n2 = nth
      count += 1
    }
  }
}