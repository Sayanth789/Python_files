# Tuples are not Just Immutable Lists 
# Tuples are used as records 

lax_coordinates = (33.9425, -118.40856)
city, year, pop, chg, area = ('Tokyo', 2003,32_450, 0.66, 8014)

traveler_ids = [('USA', '31195855'), ('BRA', 'CE34657'), ('ESP', 'XDA205856')]

for passport in sorted(traveler_ids):
    print('%s %s' % passport)

for country, _ in traveler_ids:
    print(country)    

# Tuples as Immutable Lists   
#  
a =(10, 'alpha', [1, 2])
b = (10, 'alpha', [1, 2])
print(a == b)

print(b[-1].append(99))
print(a == b)
print(b)


def fixed(o):
    try:
        hash(o)
    except TypeError: 
        return False 
    return True 

tf = (10, 'alpha', (1, 2))  # Contains no mutable items 
tm = (10, 'alpha', [1, 2])  # contains a mutable item (list)

print(fixed(tf))


print(fixed(tm))

# Unpacking sequences and iterables

lax_coordinates = (33.9425, -118.408056)
latutude, longitude = lax_coordinates 
print(latutude)

print(longitude)

print(divmod(20, 8))

t = (20, 8)
print(divmod(*t))

quotient, remainder = divmod(*t)
print(quotient, remainder)

import os 

_, filename = os.path.split('/home/luciano/.ssh/id_rsa.pub')

print(filename)

#  Using * to grab excess items 

a, b, *rest = range(5)
print(a, b, rest) 

a, b, *rest = range(3)
print(a, b, *rest)

a, b, *rest = range(2)
print(a, b, rest)

a, *body, c, d = range(5)
print(a, body, c, d)

*head, b, c, d = range(5)
print(head, b, c, d)


# Unpacking with * in function calls and sequence literals

def fun(a, b, c, d, *rest):
    return a, b, c, d, rest

print(fun(*[1, 2],3, *range(4,7)))
