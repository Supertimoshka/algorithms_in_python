def binary_search(lst, search_item):
    low = 0
    high = len(lst) - 1
    search_result = False

    while low <= high and not search_result:
        middle = (low + high) // 2
        guess = lst[middle]

        if guess == search_item:
            search_result = True
            return search_result
        if guess > search_item:
            high = middle - 1
        else:
            low = middle + 1
        
    return search_result

lst = [1, 2, 3, 4, 5, 6, 7, 8]
value = 6
result = binary_search(lst, value)

if result:
    print("Done")
else:
    print("Error")


# Разобраться