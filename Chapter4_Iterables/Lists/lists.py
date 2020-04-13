def main():
    my_list = [1, 2, 3]

    # Option 1: Single Value
    my_list.append(-10)
    print(my_list)
    # Option 2: List Concatenation
    my_list2 = [4, 5]
    #my_list += my_list2
    my_list = my_list + my_list2
    print(my_list)
    # Option 3: Iterables
    it = range(-2, 3, 1)
    my_list.extend(it)
    print(my_list)
    # Option 4: Insert at user-defined index
    my_list.insert(0, "hello")
    print(my_list)
    my_list.insert(-30, "hello")
    print(my_list)
    # Remove values
    my_list.pop()
    print(my_list)
    while 'hello' in my_list:
        idx = my_list.index('hello')
        my_list.pop(idx)
    print(my_list)
    # Copy
    my_list_new = my_list
    print(hex(id(my_list)))
    print(hex(id(my_list_new)))
    my_list_new = my_list.copy()
    print(hex(id(my_list)))
    print(hex(id(my_list_new)))
    # Reverse
    my_list.reverse()
    print(my_list)
    print(my_list[::-1])
    # Count
    print(my_list.count(1))
    # Sort
    my_list.append('hello')
    my_list.sort(reverse=True)
    print(my_list)

if __name__ == "__main__":
    main()
