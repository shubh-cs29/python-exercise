keys = ['red', 'green', 'blue']
values = ['#FF0000','#008000', '#0000FF']
dic = {}

for (i, j) in zip(keys, values):
  dic.update({i : j})

print(dic)