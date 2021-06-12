d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

sorted_tuple = sorted(d.items(), key = lambda kv:kv[1])  #kv[1]=sort by values & kv[0]=sort by keys
sorted_dict = dict(sorted_tuple)
print(sorted_dict)