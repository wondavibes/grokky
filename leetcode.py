import itertools

num = [3,1,2,10,1]
new_num = list(itertools.accumulate(num))
print(new_num)