
class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
    
    def prepend(self, value):
        self.head = Node(value, self.head)
    
    def append(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
    
    def peek(self):
        if self.head: return self.head.data
    
    def find(self, value):
        node = self.head
        while node and node.data != value:
            node = node.next
        return node is not None
    
    def pop(self):
        if self.head:
            node = self.head
            self.head = node.next
            return node
    
    def remove(self, value):
        node = self.head
        prev = None
        while node and node.data != value:
            prev = node
            node = node.next
        if node:
            if node is self.head:
                self.head = node.next
            else:
                prev.next = node.next
            if node is self.tail:
                self.tail = prev
            return True
        return False


class SortedLinkedList(LinkedList):
    def __init__(self):
        self.head = None
        self.tail = None
    
    def prepend(self, value):
        self.insert(value)
    
    def append(self, value):
        self.insert(value)
    
    def find(self, value):
        if not self.head.data < value < self.tail.data: return False
        node = self.head
        while node.data < value:
            node = node.next
        return node.data == value
    
    def insert(self, value):
        if value <= self.head.data:
            LinkedList.prepend(self, value)
        elif value >= self.tail.data:
            LinkedList.append(self, value)
        else:
            node = self.head.next
            prev = self.head
            while node.data < value:
                prev = node
                node = node.next
            new_node = Node(value)
            prev.next = new_node
            new_node.next = node
    
    def remove(self, value):
        if not self.head.data <= value <= self.tail.data: return False
        node = self.head
        prev = None
        while node.data < value:
            prev = node
            node = node.next
        if node.data != value: return False
        if node is self.head:
            self.head = node.next
        else:
            prev.next = node.next
        if node is self.tail:
            self.tail = prev
        return True


class Stack(LinkedList):
    def __init__(self):
        self.head = None
        self.size = 0
    
    def __len__(self):
        return self.size
    
    def push(self, item):
        self.prepend(item)
        self.size += 1
    
    def pop(self):
        item = LinkedList.pop(self)
        if item:
            self.size -= 1
            return item.data
        else:
            return None

    
class Queue(LinkedList):
    def __init__(self):
        LinkedList.__init__(self)
        self.size = 0
    
    def __len__(self):
        return self.size

    def enqueue(self, item):
        self.append(item)
        self.size += 1
    
    def dequeue(self):
        item = self.pop()
        if item: 
            self.size -= 1
            return item.data
        else: return None