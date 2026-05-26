try:
    num1 = int(input("Enter first integer: "))
    num2 = int(input("Enter second integer: "))
except ValueError:
    print("Error: You must enter valid integers.")
    exit() 
fun = input("+\n-\n*\n/\nEnter an operation to done : ").strip()

def add(num1,num2):
  return num1 + num2
def sub(num1,num2):
  return num1 - num2
def mul(num1,num2):
  return num1 * num2
def div(num1,num2):
  if num1 == 0 or num2 == 0:
    print("Zero Division error")
  else:
   return num1 / num2
result = None
match fun:
  case "+":
    result = add(num1,num2)
  case "-":
    result = sub(num1,num2)
  case "*":
    result = mul(num1,num2)
  case "/":
    result = div(num1,num2)
  case _:
    print("Invalid")
if result is not None:
  print(f"Answer = {result}")

  
  

