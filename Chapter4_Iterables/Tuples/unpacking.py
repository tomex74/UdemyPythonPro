s = 'Hello'

a, b, c, d, e = s
print(a)
print(b)
print(c)
print(d)
print(e)

t = (42, 5, 25)
x, y, z = t

l = [1, 2, 3]
a, *b = l # * always unpacks into a list
print(type(b))

l = (1, 2, 3)
a, *b = l # * always unpacks into a list
print(type(b))
