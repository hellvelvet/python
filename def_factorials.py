def factorials(n):
  fact = {}
  for i in range(1, n+1):
    f = 1
    for j in range(1, i+1):
      f *= j
    fact[i] = f
  return fact


k = factorials(5)
print(k[1]) 
print(k[3])
print(k[5])