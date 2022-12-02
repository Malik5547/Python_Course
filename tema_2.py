
my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

if __name__ == '__main__':
    sorted_list = my_list.copy()
    sorted_list.sort()
    print(sorted_list)

    d_sorted_list = my_list.copy()
    d_sorted_list.sort(reverse=True)
    print(d_sorted_list)
    
    even_list = my_list[::2]
    print(even_list)

    odd_list = my_list[1::2]
    print(odd_list)

    multiples_of_3 = [elem for elem in my_list if (elem % 3) == 0]
    print(multiples_of_3)