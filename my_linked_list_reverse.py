class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def reverse(head):
    current = head
    previous = None
    next = None

    while current is not None:
        next = current.next
        current.next = previous

        previous = current
        current = next

    return previous


def printlist(head):
    result = ""

    current = head
    while current:
        result += str(current.value) + " -> "
        current = current.next

    print(result)


head = Node(1, Node(2, Node(3)))

printlist(head)

head = reverse(head)
printlist(head)