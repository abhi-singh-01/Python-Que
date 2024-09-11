def fibonacci(n):
  """
  This function prints the Fibonacci series up to n.
  """
  if n < 0:
    print("Incorrect input")
    return
  elif n == 0:
    print(0)
  elif n == 1:
    print(1)
  else:
    a, b = 0, 1
    for i in range(n):
      print(a, end=" ")
      a, b = b, a + b

# Number of terms to print
n = int(input("Enter the no. of terms:"))

# Print fibonacci series
fibonacci(n)
