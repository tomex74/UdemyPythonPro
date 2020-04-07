# Boolean Operators: not, and, or

# Rules:
# A or B == B or A
# A and B == B and A
# A and (B or C) == (A nad B) or (A and C)
# not(A or B) == (not A) and (not B)
# not(A and B) == (not A) or (not B)

# Comparison operators: <, >, <=, >=, ==, !=, in, is

# Operator Precedence:
# 1.) ()
# 2.) Comparison operators
# 3.) not
# 4.) and
# 5.) or

# Bad example
a = True
b = False
c = True
statement = a > b and c == a or not a and c
print(statement)

# Better example
statement = ((a != b) and (c == a)) or ((not a) and c)
print(statement)
