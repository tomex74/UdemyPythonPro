my_var1 = 10
print(hex(id(my_var1)))
my_var1 = my_var1 + 10
print(hex(id(my_var1)))
my_var1 = 12
print(hex(id(my_var1)))

class A:
    def __init__(self, v):
        self.v = v

a = A(10)
print(hex(id(a)), hex(id(a.v)))
a.v = 12
print(hex(id(a)), hex(id(a.v)))

def process_str(s):
    s = s + ' added'
    return s

s = 'hello'
print(s, hex(id(s)))
# process_str(s)
s = process_str(s)
print(s, hex(id(s)))

def process_list(l):
    l.append(42)

l = [1, 2]
other_l = l
another_l2 = [1, 2]
print(l, hex(id(l)))
process_list(l)
print(l, hex(id(l)))
print(other_l)
print(hex(id(another_l2)))
