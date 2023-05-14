def carre(x):
  return x * x

print(carre(2))
print('-' * 40)

# en utilisant une fonction lambda
carreLambda = lambda x: x * x

print(carreLambda(10))
print('-' * 40)


# en utilisant la fonction map
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
carreMap = map(lambda x: x * x, nums)
for num in carreMap:
  print(num)