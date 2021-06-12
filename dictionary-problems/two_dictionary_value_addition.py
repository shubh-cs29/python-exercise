d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d3 = {}

for (k1, v1), (k2, v2) in zip(d1.items(), d2.items()):
  value_addition = v1 + v2
  d3.update({k1: value_addition})

print(d3)