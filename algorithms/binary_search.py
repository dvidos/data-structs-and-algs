import random, string, timeit

def create_random_string():
    return ''.join(random.choice(string.ascii_letters) for x in range(random.randint(5, 10)))

def create_random_array(size: int):
    random_target_pos = random.randint(0, size - 1);
    a = []
    for i in range(size):
        if i == random_target_pos:
            a.append("needle")
        a.append(create_random_string())
    return a

def search_linearly(arr, item):
    for i in range(len(arr)):
        if arr[i] == item:
            return i
    return -1

def search_binary(arr, item):
    # sorted array is assumed
    lower = 0
    upper = len(arr) - 1
    while upper > lower:
        midPoint = (upper + lower) // 2
        mid = arr[midPoint]
        if mid == item:
            return midPoint
        elif item < mid:
            upper = midPoint
        else:
            lower = midPoint
    return -1
        

def test():
    size = 100000
    print(f"Generating random array of {size} items")
    a = create_random_array(size)
    sorted_a = a.copy()
    sorted_a.sort()

    for i in range(10):
        print(f"  a[{i}] = \"{a[i]}\"")
    for i in range(10):
        print(f"  sorted_a[{i}] = \"{sorted_a[i]}\"")
    
    print("Linear search...");
    print("{:.6f}".format(timeit.timeit(lambda: search_linearly(a, "needle"), number=1000)))
    print("Binary search...")
    print("{:.6f}".format(timeit.timeit(lambda: search_binary(sorted_a, "needle"), number=1000)))


test()
"""
Generating random array of 100000 items
  a[0] = "WnpNyz"
  a[1] = "maiEIc"
  a[2] = "wqjCG"
  a[3] = "fJAQe"
  a[4] = "dsiglAKj"
  a[5] = "XUZUBjzZ"
  a[6] = "KAWNK"
  a[7] = "GsdfSDA"
  a[8] = "VTQVIIclO"
  a[9] = "OpNMCcKMT"
  sorted_a[0] = "AABGKS"
  sorted_a[1] = "AABJSBJhUC"
  sorted_a[2] = "AABphhDrg"
  sorted_a[3] = "AACtxd"
  sorted_a[4] = "AADBRZrIKn"
  sorted_a[5] = "AADQTBq"
  sorted_a[6] = "AAFGUjw"
  sorted_a[7] = "AAFOhy"
  sorted_a[8] = "AAIlSbH"
  sorted_a[9] = "AAJslkHV"
Linear search...
3.397247
Binary search...
0.001615
"""