# Rounding

val_float = 42.4242424224
print(type(val_float), val_float)
val_int = int(val_float)
print(type(val_int), val_int)
val_int = round(val_float, 0) # 0 is the default value 
print(type(val_int), val_int)
val_int = round(val_float, 2) 
print(type(val_int), val_int)

val_int = round(val_float, -1) # Round the next multiple of 10
print(type(val_int), val_int)
val_int = round(val_float, -2) # Round the next multiple of 100
print(type(val_int), val_int)
val_int = round(18.2, -1)
print(type(val_int), val_int)
