#Create a program that swaps the values of two variables

x = input("Enter first value:")
y = input("Enter second value:")

def swap_var (x, y):
  x , y = y, x

  print('After swap: ', x, y)
swap_var(x, y)
