import random


def swap(array, index1, index2):
    temp = array[index1]
    array[index1] = array[index2]
    array[index2] = temp


def is_in_order(array):
    for i in range(1, len(array)):
        if array[i] < array[i-1]:
            return False
    return True


def generate_int_array(size):
    return [random.randint(0, size) for x in range(size)]


def __hash__(arr):
    hash_total = 0
    for x in arr:
        hash_total *= hash(x)
    return hash_total


def select_sort(array):
    for i in range(len(array)):
        smallest = i
        for j in range(i + 1, len(array)):
            if array[smallest] > array[j]:
                smallest = j
        swap(array, smallest, i)


def insert_sort(array):
    for i in range(1, len(array)):
        ptr = i
        while ptr > 0 and array[ptr - 1] > array[ptr]:
            swap(array, ptr - 1, ptr)
            ptr -= 1


def bubble_sort(array):
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, len(array)):
            if array[i - 1] > array[i]:
                swap(array, i - 1, i)
                swapped = True


def merge_sort(array):
    if len(array) > 1:
        mid = len(array)//2

        left = array[:mid]
        right = array[mid:]

        merge_sort(left)
        merge_sort(right)

        i_left = 0
        i_right = 0
        i_sorted = 0

        while i_left < len(left) and i_right < len(right):
            if left[i_left] < right[i_right]:
                array[i_sorted] = left[i_left]
                i_left += 1
            else:
                array[i_sorted] = right[i_right]
                i_right += 1
            i_sorted += 1
        while i_left < len(left):
            array[i_sorted] = left[i_left]
            i_left += 1
            i_sorted += 1
        while i_right < len(right):
            array[i_sorted] = right[i_right]
            i_right += 1
            i_sorted += 1


def shell_sort(array):
    gap = len(array)//2
    while gap > 0:
        for x in range(gap, len(array), 1):
            shell_insert(array, x, gap)
        if gap == 2:
            gap = 1
        else:
            gap = gap // 2.2
            gap = int(gap)


def shell_insert(array, index, gap):
    temp = array[index]
    while index > gap-1 and temp < array[index-gap]:
        array[index] = array[index-gap]
        index -= gap
    array[index] = temp


def quick_sort(array, start, end):
    if start < end:
        pivot = quick_partition(array, start, end)

        quick_sort(array, start, pivot-1)
        quick_sort(array, pivot+1, end)


def quick_partition(array, start, end):
    mid = (end-start)/2
    mid = int(mid)

    if array[mid] < array[start]:
        swap(array, mid, start)
    if array[mid] > array[end]:
        swap(array, mid, end)
    if array[start] > array[mid]:
        swap(array, mid, start)

    left_ptr = start
    right_ptr = end

    swap(array, mid, start)
    pivot = array[start]
    done = False
    while not done:
        print("left ".join(str(left_ptr)))
        print("right ".join(str(right_ptr)))
        while left_ptr < end and pivot >= array[left_ptr]:
            left_ptr += 1
        while right_ptr > start and pivot < array[right_ptr]:
            right_ptr -= 1
        if left_ptr < right_ptr:
            swap(array, left_ptr, right_ptr)
        if left_ptr > right_ptr:
            done = True
    swap(array, start, right_ptr)
    return right_ptr
