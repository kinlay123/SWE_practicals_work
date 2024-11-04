class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """Append an item to the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        """Display the list in a readable format."""
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))

    def insert(self, data, position):
        """Insert an item at a specified position."""
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(position - 1):
            if current is None:
                raise IndexError("Position out of range")
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def delete(self, data):
        """Delete the first occurrence of a specified item."""
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def search(self, data):
        """Search for an item and return its position. Return -1 if not found."""
        current = self.head
        position = 0
        while current:
            if current.data == data:
                return position
            current = current.next
            position += 1
        return -1

    def reverse(self):
        """Reverse the linked list."""
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def find_middle(self):
        """Find the middle element of the linked list."""
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data if slow else None

    def has_cycle(self):
        """Detect if the linked list has a cycle using Floyd's Tortoise and Hare algorithm."""
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def remove_duplicates(self):
        """Remove duplicates from an unsorted linked list."""
        current = self.head
        seen = set()
        prev = None
        while current:
            if current.data in seen:
                prev.next = current.next  
            else:
                seen.add(current.data)
                prev = current
            current = current.next

    def merge_sorted(self, other):
        """Merge two sorted linked lists into a single sorted linked list."""
        dummy = Node(0)
        tail = dummy
        l1, l2 = self.head, other.head
        
        while l1 and l2:
            if l1.data < l2.data:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        
        tail.next = l1 or l2  
        return dummy.next  
ll1 = LinkedList()
ll1.append(1)
ll1.append(3)
ll1.append(5)
ll1.append(7)
print("First Linked List:")
ll1.display()
ll2 = LinkedList()
ll2.append(2)
ll2.append(4)
ll2.append(6)
ll2.append(8)
print("\nSecond Linked List:")
ll2.display()  
merged_list_head = ll1.merge_sorted(ll2)
print("\nMerged Sorted Linked List:")
merged_list = LinkedList()
merged_list.head = merged_list_head
merged_list.display()  

print("\nMiddle element of the first linked list:", ll1.find_middle())  


print("Does the first linked list have a cycle?", ll1.has_cycle()) 


ll_with_duplicates = LinkedList()
ll_with_duplicates.append(1)
ll_with_duplicates.append(2)
ll_with_duplicates.append(2)
ll_with_duplicates.append(3)
ll_with_duplicates.append(1)
print("\nLinked List with duplicates:")
ll_with_duplicates.display()  
ll_with_duplicates.remove_duplicates()
print("After removing duplicates:")
ll_with_duplicates.display()  
