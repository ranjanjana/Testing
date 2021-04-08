import itertools 
s = {1, 2, 3, 4} 
n = 3
x= list(itertools.combinations(s, n)) 
print(x)
print(len(x))
print(x[0])
print(list(x[0]))