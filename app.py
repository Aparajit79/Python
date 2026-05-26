# temp calculator 
while True:
 try:
  temp_cel = float(input("Enter the temperature in celcius = "))
  break
 except ValueError:
  print("Invalid input , please enter a valid numerical value")
fahrenheit = (temp_cel * 9/5 )+ 32
print(fahrenheit) 