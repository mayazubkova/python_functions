
def binary(number): #converting decimal number to binary
  binar = ''
  while number > 0:
    binar = str(number % 2) + binar
    number = number // 2
  return binar


def multiply(): #multiplying two inputs while making sure they're both integers
  while True:
    try:  
      x = input('enter a number: ')
      y = input('enter another number: ')
      answer = int(x)*int(y)
      break
    except:
      print('please enter a valid number')

  return answer



