dic = {'x':500, 'y':5874, 'z': 560, 's':900}

# sorted_tuple = sorted(dic.items(), key = lambda kv: kv[1])
# sorted_dic = dict(sorted_tuple)
# print(sorted_dic.values())
# res = list(sorted_dic.values())[-1]
# print(res)

dic_values = dic.values()
val_list = list(dic_values)
val_list_len = len(val_list) - 1
val_list.sort()
print(val_list[val_list_len])