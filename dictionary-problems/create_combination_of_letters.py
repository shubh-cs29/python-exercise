dic = {'1':['a','b'], '2':['c','d']}

dict_values =  dic.values()
lst = list(dict_values)

for (l1) in zip(lst):
    lst_len = len(l1)
    print(l1[0][1])