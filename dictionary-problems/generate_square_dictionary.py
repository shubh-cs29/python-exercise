dic_size = 5
dic = {}

# while dic_size > 0:
#   k = dic_size
#   v = dic_size * dic_size
#   dic.update({k: v})
#   dic_size = dic_size - 1
#
# print(dict(reversed(list(dic.items()))))

###### We can do this using while loop OR for loop

for i in range(0, dic_size+1):
  if i == 0:
    i = 1
    dic.update({i: i * i})
  else:
    dic.update({i: i * i})

print(dic)