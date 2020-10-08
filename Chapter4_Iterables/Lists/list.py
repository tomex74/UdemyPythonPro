def main():
    my_list =[1, 2, 3]

    #Option 1: Single Value
    my_list.append(-10)
    print(my_list)
    #Option 2 : List Concatenation
    my_list2 = [4 ,5]
    my_list += my_list2
    print(my_list)
    #Option 3 : Iterables
    it = range(-2, 3, 1)
    my_list.extend(it)
    print(my_list)
    





if __name__== "__main__":
    main()
