numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# filter(lambda, numbers)
paires = list(filter(lambda x: x%2 == 0, numbers ))

print(paires)

impaires = list(filter(lambda x: x%2 != 0, numbers ))

print(impaires)

# filtrer les personnes qui on 26 ans
friends = [
  {"name": "alex", "age": 26},
  {"name": "pierre", "age": 12},
  {"name": "leo", "age": 46},
  {"name": "justine", "age": 26},
  {"name": "manon", "age": 88},
  {"name": "sophie", "age": 26},
]

friendFilterParAge = list(filter(lambda f: f["age"] == 26 , friends))
print(friendFilterParAge)