dic = {'red': '#FF0000', 'green': '#008000', 'blue': '#0000FF'}

sorted_tuple = sorted(dic.items(), key = lambda kv: kv[0])
sorted_dict = dict(sorted_tuple)
print(sorted_dict)