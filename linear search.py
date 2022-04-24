def linear_search(lst, search_item):
    index = 0
    search_results = False

    while index < len(lst) and not search_results:
        if lst[index] == search_item:
            search_results = True
        else:
            index += 1
    
    return search_results

lst = [1, 12, 35, 6, 8, 10, 11]
value = 12
result = linear_search(lst, value)

if result:
    print("Элемент найден")
else:
    print("Элемент не найден")

