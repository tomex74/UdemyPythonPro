# Lambda Expressions are local function objects

# Syntax:
# lambda [param list]: expression

# Rules:
# Do not use the word 'return'
# Single expression (simple expressions)
# No Assignments
lamb = lambda x, y: x + y
print(dir(lamb))

a = 2
b = 3

print(lamb(a, b))