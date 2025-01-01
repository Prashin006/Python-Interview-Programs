from jmespath.ast import current_node


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        """Define behaviour of len()."""
        return self.size

    def __getitem__(self, index):
        """Enables indexing mechanism (obj[index])."""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range!")
        current = self.head
        for _ in range(index):
            current = current.next
        return current.value

    def __setitem__(self, index, value):
        """Enables item assignment (obj[index] = value)."""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range!")
        current = self.head
        for _ in range(index):
            current = current.next
        current.value = value

    def __delitem__(self, index):
        """Delete an item (del obj[index])."""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range!")
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            current.next = current.next.next
        self.size -= 1

    def __contains__(self, value):
        """Defines behaviour for 'in' keyword"""
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def append(self, value):
        """Adds a new node to the end of the linked list"""
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.size += 1

    def __str__(self):
        """User-friendly string representation"""
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        return "->".join(values)

# Example usage
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
print(len(ll))
print(ll[1])
ll[1] = 36
print(ll)
del ll[1]
print(ll)
print("10 in ll:", 10 in ll)