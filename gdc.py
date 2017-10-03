def gcd(number1, number2):
  if number1 > number2:
    big = number1
    small = number2
  elif number2 > number1:
    big = number1
    small = number2
  else:
    return number1
  while big%small != 0:
    small = small - (big % small)
  return small


print (cd(144,4))
