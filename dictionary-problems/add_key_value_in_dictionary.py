d = {0: 10, 1: 20}
for k,v in d.items():
  key = k + 1
  val = v + 10

d.update({key:val})
print(d)