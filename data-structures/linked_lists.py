import random, timeit

# ideally these lists are really fitted for C/C++, but
# we have to work with a language for interviews.

class SingleLinkNode:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

def generate_singly_link_list(count) -> SingleLinkNode:
    head = None
    for i in range(count):
        node = SingleLinkNode(random.randint(0, 65535))
        node.next = head # inserting at head for generation speed
        head = node
    return head

def get_singly_linked_list_node(head: SingleLinkNode, index):
    node = head
    while index > 0 and node != None:
        node = node.next
        index -= 1
    return node

def append_singly_linked_list_node(head: SingleLinkNode, node: SingleLinkNode):
    # we need to find the end
    if head == None:
        head = node
    else:
        trailing = head
        while trailing.next != None:
            trailing = trailing.next
        trailing.next = node
    
    return head

def remove_singly_linked_list_node(head: SingleLinkNode, node: SingleLinkNode):
    # we need the trailing node, so we need to traverse from start
    trailing = head
    while trailing.next != node:
        trailing = trailing.next
    if trailing == None:
        return
    
    trailing.next = node.next
    node.next = None
    return head


# ----------------------------------------------------------------


class DoubleLinkNode:
    def __init__(self, value) -> None:
        self.value = value
        self.next: DoubleLinkNode = None
        self.prev: DoubleLinkNode = None

def generate_doubly_linked_list(count):
    head = None
    tail = None
    for i in range(count):
        node = DoubleLinkNode(random.randint(0, 65535))
        if tail == None:
            head = node
            tail = node
        else:
            tail.next = node
            node.prev = tail
            node.next = None
            tail = node
    return [head, tail]

def get_doubly_linked_list_node(head: DoubleLinkNode, index):
    node = head
    while index > 0 and node != None:
        node = node.next
        index -= 1
    return node

def append_doubly_linked_list_node(head: DoubleLinkNode, tail: DoubleLinkNode, node: DoubleLinkNode):
    # we can append at the tail immediately
    if tail == None:
        head = node
        tail = node
    else:
        tail.next = node
        node.prev = tail
        node.next = None
        tail = node
    return head, tail

def remove_doubly_linked_list_node(head: DoubleLinkNode, tail: DoubleLinkNode, node: DoubleLinkNode):
    if node == head:
        # update head
        head = head.next
        head.prev = None
    elif node == tail:
        # update tail
        tail = node.prev
        tail.next = None
    else:
        # just remove from the middle
        node.prev.next = node.next
        node.next.prev = node.prev
    return [head, tail]


# ----------------------------------------------------------------

def test_single_list_ops(head, index):
    new_node = SingleLinkNode(9999)
    head = append_singly_linked_list_node(head, new_node)
    head = remove_singly_linked_list_node(head, new_node)


def test_double_list_ops(head, tail, index):
    new_node = DoubleLinkNode(9999)
    [head, tail] = append_doubly_linked_list_node(head, tail, new_node)
    [head, tail] = remove_doubly_linked_list_node(head, tail, new_node)


def test():
    items = 100 # 10000000

    print(f"Generating single linked list with {items} items...")
    head = generate_singly_link_list(items)

    print(f"Generating double linked list with {items} items...")
    [head, tail] = generate_doubly_linked_list(items)

    started = timeit.default_timer()
    test_single_list_ops(head, items - 5)
    elapsed = timeit.default_timer() - started
    print(f"  Single list append & delete: {elapsed:.6f}")

    started = timeit.default_timer()
    test_double_list_ops(head, tail, items - 5)
    elapsed = timeit.default_timer() - started
    print(f"  Double list append & delete: {elapsed:.6f}")


test()
"""
Generating single linked list with 100 items...
Generating double linked list with 100 items...
  Single list append & delete: 0.000017
  Double list append & delete: 0.000006


Generating single linked list with 10000000 items...
Generating double linked list with 10000000 items...
  Single list append & delete: 1.098934
  Double list append & delete: 0.000014
"""
