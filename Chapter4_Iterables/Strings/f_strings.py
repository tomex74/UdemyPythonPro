a = 10
b = 3
c = 10 % b

# Old format
print('%d %s %d = %d' % (a, '%', b, c))

# Old-New format
print('{} % {} = {}'.format(a, b, c))
print('{0} % {1} = {2}'.format(a, b, c))

# New f-Strings
print(f'{a} % {b} = {c}')

print(f'{True == True}')