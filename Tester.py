from Sorting import Sorter

arraySize = 20

arr = Sorter.generate_int_array(arraySize)
preSort = Sorter.__hash__(arr)
print("Array before bubble sort: ")
print(arr)
print("Array after bubble sort: ")
Sorter.bubble_sort(arr)
print(arr)
if preSort == Sorter.__hash__(arr) and Sorter.is_in_order(arr):
    print("Array was successfully sorted with bubble sort\n")
else:
    print("Array was unsuccessfully sorted with bubble sort\n")


arr = Sorter.generate_int_array(arraySize)
preSort = Sorter.__hash__(arr)
print("Array before insertion sort: ")
print(arr)
print("Array after insertion sort: ")
Sorter.insert_sort(arr)
print(arr)
if preSort == Sorter.__hash__(arr) and Sorter.is_in_order(arr):
    print("Array was successfully sorted with insertion sort\n")
else:
    print("Array was unsuccessfully sorted with insertion sort\n")


arr = Sorter.generate_int_array(arraySize)
preSort = Sorter.__hash__(arr)
print("Array before selection sort: ")
print(arr)
print("Array after selection sort: ")
Sorter.select_sort(arr)
print(arr)
if preSort == Sorter.__hash__(arr) and Sorter.is_in_order(arr):
    print("Array was successfully sorted with selection sort\n")
else:
    print("Array was unsuccessfully sorted with selection sort\n")

arr = Sorter.generate_int_array(arraySize)
preSort = Sorter.__hash__(arr)
print("Array before merge sort: ")
print(arr)
print("Array after merge sort: ")
Sorter.merge_sort(arr)
print(arr)
if (preSort == Sorter.__hash__(arr)) and Sorter.is_in_order(arr):
    print("Array was successfully sorted with merge sort\n")
else:
    print("Array was unsuccessfully sorted with merge sort\n")

arr = Sorter.generate_int_array(arraySize)
preSort = Sorter.__hash__(arr)
print("Array before shell sort: ")
print(arr)
print("Array after shell sort: ")
Sorter.shell_sort(arr)
print(arr)
if (preSort == Sorter.__hash__(arr)) and Sorter.is_in_order(arr):
    print("Array was successfully sorted with shell sort\n")
else:
    print("Array was unsuccessfully sorted with shell sort\n")

arr = Sorter.generate_int_array(arraySize)
preSort = Sorter.__hash__(arr)
print("Array before quick sort: ")
print(arr)
print("Array after quick sort: ")
Sorter.quick_sort(arr, 0, len(arr)-1)
print(arr)
if (preSort == Sorter.__hash__(arr)) and Sorter.is_in_order(arr):
    print("Array was successfully sorted with quick sort\n")
else:
    print("Array was unsuccessfully sorted with quick sort\n")