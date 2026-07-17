def is_even(number):
  if(number % 2 == 0):
    print("Number is even")
  else:
    print("Odd number")

is_even(10)


def largest(a, b, c):
  if(a > b and a > c):
    print("A is largest")
  elif(b > a and b > c):
    print("B is largest")
  else:
    print("C is largest")

largest(10, 20, 30)

def reverse_string(text):
    reverse_text = " "
    for letter in text:
        reverse_text = letter + reverse_text
    print(reverse_text)


   
reverse_string("hello")


def count_vowels(text):
  vowels = 0
  for l in text:
    if(l == 'a' or l == 'e' or l == 'i' or l == 'o' or l == 'u'):
      vowels = vowels + 1
  print(vowels)

count_vowels("hello")


def fibonacci(n):
  if n <= 0:
    return []
  elif n == 1:
    return [0]
  else:
    fib_series = [0, 1]
    while len(fib_series) < n:
      next_number = fib_series[-1] + fib_series[-2]
      fib_series.append(next_number)
    return fib_series
