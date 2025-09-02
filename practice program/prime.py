num = int(input("enter a number"))
def prime_factors(num):
  factors = []
  factor = 2

  while (num >= 2):
    if (num % factor == 0):
      factors.append(factor)
      num = num / factor
    else:
      factors += 1
  return factors
print(num)
#prime_factors(13195)# [2,2,3]
