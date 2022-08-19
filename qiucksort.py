import random

def quicksort(array, elem_from, elem_to):
    if elem_from >= elem_to:
        return

    i, j = elem_from, elem_to
    elem = random.randint(elem_from, elem_to)

    while i <= j:
        while array[i] < array[elem]:
            i += 1
        while array[j] > array[elem]:
            j -= 1
        
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i, j = i + 1, j - 1
    
    quicksort(array, elem_from, j)
    quicksort(array, i, elem_to)

a = [4, 9, 7, 6, 2, 3, 8]
quicksort(a, 0, len(a) - 1)
print(a)
