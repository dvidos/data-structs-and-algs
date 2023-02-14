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


def quick_sort(arr: list) -> list:
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
    print("a = " + str(a[:8]) + "...")

    a1 = a.copy()
    a2 = a.copy()
    a3 = a.copy()

    print("Bubble sort...");
    print("{:.6f}".format(timeit.timeit(lambda: bubble_sort(a1), number=1)))
    print("  sorted = " + str(a1[:8]) + "...")

    print("Merge sort...")
    print("{:.6f}".format(timeit.timeit(lambda: merge_sort(a2), number=1)))
    print("  sorted = " + str(a2[:8]) + "...")

    print("Quick sort...")
    print("{:.6f}".format(timeit.timeit(lambda: quick_sort(a3), number=1)))
    print("  sorted = " + str(a3[:8]) + "...")

test()