# Assigning to Slices

l = list(range(10))

print(l)

l[2:5] = [20, 30]
print(l)

del(l[5:7])
print(l)

l[3::2] = [11, 22]
print(l)

# By design this raises an Exception 
try:
    l[2:5] = 100 
except Exception as e:
    print(repr(e))

l[2:5] = [100]
print(l)    
