# linkedlists.py
# Implements a linked list data structure, and several data structures
# that extend and modify the linked list. 
#
# Copyright 2011, Mark Tupala.
# All rights reserved.
#
# Created: Mark Tupala (tupala@ualberta.ca)

class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class DNode(Node):
    def __init__(self, data, next=None, prev=None):
        super(DNode, self).__init__(data, next)
        self.prev = prev


class LinkedList(object):
    def __init__(self):
        self.head = None
    
    # ACCESSORS
    def first(self):
        try: return self.head.data
        except: return None
    
    def last(self):
        node = self.head
        while node:
            data = node.data
            node = node.next
        try: return data
        except: return None
    
    def find(self, value):
        node = self.head
        while node and node.data != value:
            node = node.next
        return node is not None

    def traverse(self, *funcs):
        node = self.head
        while node is not None:
            temp = funcs[0](node.data)
            for func in funcs[1:]:
                temp = func(temp)
            node = node.next

    # MUTATORS
    def clear(self):
        self.head = None
    
    def prepend(self, value):
        self.head = Node(value, self.head)
    
    def pop(self):
        try:
            node = self.head
            self.head = node.next
            return node.data
        except: return None
    
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
            return True
        return False

class TailList(LinkedList):
    def __init__(self):
        super(TailList, self).__init__()
        self.tail = None
    
    # ACCESSORS
    def last(self):
        try: return self.tail.data
        except: return None
    
    # MUTATORS
    def clear(self):
        super(TailList, self).clear()
        self.tail = None

    def prepend(self, value):
        super(TailList, self).prepend(value)
        if not self.head.next: self.tail = self.head
    
    def append(self, value):
        node = Node(value)
        self.link(node)

    def link(self, node):
        if not self.head:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node

    def pop(self):
        data = super(TailList, self).pop()
        if not self.head: self.tail = None
        return data

    def remove(self, value):
        node = self.head
        prev = None
        while node and node.data != value:
            prev = node
            node = node.next
        if not node: return False
        if node is self.head:
            self.pop()
        elif node is self.tail:
            self.tail = prev
        else:
            prev.next = node.next
        return True

class DoubleLinkedList(TailList):
    def __init__(self):
        super(DoubleLinkedList, self).__init__()
    
    # ACCESSORS
    def rev_traverse(self, *funcs):
        node = self.tail
        while node is not None:
            temp = funcs[0](node.data)
            for func in funcs[1:]:
                temp = func(temp)
            node = node.prev

    def rev_print(self):
        node = self.tail
        while node is not None:
            print(node.data, end=' ')
            node = node.prev
        print('')
    
    # MUTATORS
    def prepend(self, value):
        dnode = DNode(value, self.head)
        if self.head: self.head.prev = dnode
        self.head = dnode
        if not self.head.next: self.tail = self.head

    def append(self, value):
        node = DNode(value, None, self.tail)
        self.link(node)

    def pop(self):
        data = super(DoubleLinkedList, self).pop()
        if self.head: self.head.prev = None
        return data

    def chop(self):
        node = self.tail
        try: self.tail = node.prev
        except: return None
        if self.tail: self.tail.next = None
        else: self.head = None
        return node.data

    def remove(self, value):
        node = self.head
        while node and node.data != value:
            node = node.next
        if not node: return False
        if node is self.head:
            self.pop()
        elif node is self.tail:
            self.chop()
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        return True


class Stack(DoubleLinkedList):
    def __init__(self):
        super(Stack, self).__init__()
        self.size = 0
    
    # ACCESSORS
    def __len__(self):
        return self.size
    
    def peek(self):
        return self.first()
    
    # MUTATORS
    def clear(self):
        super(Stack, self).clear()
        self.size = 0
    
    def push(self, item):
        self.prepend(item)
        self.size += 1
    
    def pop(self):
        item = super(Stack, self).pop()
        if item is not None: self.size -= 1
        return item

