import random, string, timeit

def create_random_string():
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(5, 10)))

def create_random_array(size: int):
    return [create_random_string() for _ in range(size)]





def merge_sort(arr: list) -> list:
    # idea is split the array in half, 
    # recurse into sorting the halves,
    # then merge the sorted paths, using sorted merge.

    if len(arr) == 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # sorted merge
    l = 0
    r = 0
    a = 0
    while l < len(left_half) or r < len(right_half):
        if l < len(left_half) and r < len(right_half):
            # compare
            if left_half[l] <= right_half[r]:
                arr[a] = left_half[l]
                l += 1
            else:
                arr[a] = right_half[r]
                r += 1
        elif l < len(left_half):
            # copy first
            arr[a] = left_half[l]
            l += 1
        elif r < len(right_half):
            # copy second
            arr[a] = right_half[r]
            r += 1
        a += 1
    
    return arr



def _qsort_partition(arr, start, end):
    # pick a pivot point (the last element in our case)
    # swap all the items larger than the pivot item to its right.
    # finally, swap the pivot item to the correct location.
    # return that pivotal final location
    pivot_point = end - 1
    pivot_value = arr[pivot_point]
    smalls_count = 0
    for i in range(start, end):
        if arr[i] < pivot_value:
            # stash all "small" values at the start
            tmp = arr[start + smalls_count]
            arr[start + smalls_count] = arr[i]
            arr[i] = tmp
            smalls_count += 1
    # put the pivot value at correct place
    tmp = arr[start + smalls_count]
    arr[start + smalls_count] = arr[pivot_point]
    arr[pivot_point] = tmp
    return start + smalls_count  # the position of the pivot in the group


def _qsort_at(arr, start, end):
    if start + 1 >= end:
        return
    # pivotal is to partition the array in linear time, 
    # placing all lower than the pivot to the left, all greater to the right
    partition_point = _qsort_partition(arr, start, end)
    _qsort_at(arr, start, partition_point)
    _qsort_at(arr, partition_point + 1, end)


def quick_sort(arr: list) -> list:
    _qsort_at(arr, 0, len(arr))
    return arr


def bubble_sort(arr: list) -> list:
    # idea is to walk the array, flipping with the next when a larger is found
    # repeat until no more flips are found
    done = False
    while not done:
        flipped = False
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                swap = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = swap
                flipped = True
        done = not flipped
    return arr



def test():
    size = 10000
    print(f"Creating random array of {size} items")
    a = create_random_array(size)
    print("  a = " + str(a[:8]) + "...")

    a1 = a.copy()
    a2 = a.copy()
    a3 = a.copy()

    print("Bubble sort...");
    print("  {:.6f}".format(timeit.timeit(lambda: bubble_sort(a1), number=1)))
    print("  sorted = " + str(a1[:8]) + "...")

    print("Merge sort...")
    print("  {:.6f}".format(timeit.timeit(lambda: merge_sort(a2), number=1)))
    print("  sorted = " + str(a2[:8]) + "...")

    print("Quick sort...")
    print("  {:.6f}".format(timeit.timeit(lambda: quick_sort(a3), number=1)))
    print("  sorted = " + str(a3[:8]) + "...")



test()
"""
Creating random array of 10000 items
  a = ['wrsvahxxa', 'hljsb', 'dplpnqfor', 'dtjeikj', 'jgxvrc', 'wvjfeh', 'hyoqc', 'aecbbgyvgs']...
Bubble sort...
  8.418231
  sorted = ['aacjplpk', 'aacuvd', 'aajmaj', 'aajmxgg', 'aakbu', 'aamyxmqq', 'aaoplgzlcz', 'aaqlpc']...
Merge sort...
  0.024804
  sorted = ['aacjplpk', 'aacuvd', 'aajmaj', 'aajmxgg', 'aakbu', 'aamyxmqq', 'aaoplgzlcz', 'aaqlpc']...
Quick sort...
  0.017305
  sorted = ['aacjplpk', 'aacuvd', 'aajmaj', 'aajmxgg', 'aakbu', 'aamyxmqq', 'aaoplgzlcz', 'aaqlpc']...
"""
