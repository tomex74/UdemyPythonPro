# 'is' and 'is not' are for for memory equality
# '==' and '!=' is for value equality
# So we can compare the data or the memory adress

# Is: Identity comparator for memory adresses (only useful for )
# Equlaity: Comparator for the object state (data/contents)

my_var1 = 10
my_var2 = my_var1

print(my_var1 == my_var2)
print(my_var1 is my_var2)

my_list1 = [1, 2]
my_list2 = [1, 2]
print(my_list1 == my_list2)
print(my_list1 is my_list2) # Important!!!

my_number1 = 42
my_number2 = 42.0
print(my_number1 == my_number2)
print(my_number1 is my_number2) # Important!!!