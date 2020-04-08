import time
from datetime import datetime

print(datetime.utcnow())

# Bad
def print_date(date=datetime.utcnow()):
    print(date)

print_date()
print_date()
print_date(datetime.utcnow())
print_date('2010-04-07 14:18:41.532911')

# Good
def print_date(date=None):
    date = datetime.utcnow() if date is None else date
    print(date)

print_date()
#time.sleep(2)
print_date()

# Bad
def own_append(v, l=[]):
    l.append(v)
    return l

my_list = []
own_append(2, my_list)
print(my_list)

my_list2 = own_append(2)
print(my_list2)

my_list3 = own_append(3)
print(my_list3) # broken

# Good
def own_append(v, l=None):
    l = [] if l is None else l
    l.append(v)
    return l

my_list2 = own_append(2)
print(my_list2)

my_list3 = own_append(3)
print(my_list3) # broken
