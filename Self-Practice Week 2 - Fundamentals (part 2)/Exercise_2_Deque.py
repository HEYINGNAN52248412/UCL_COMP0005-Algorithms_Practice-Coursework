class ListNode():
    def __init__ (self, val):
        self.val = val
        self.next = None
        self.pre = None

class Deque:
    def __init__(self):
        self.head = ListNode(None)
        self.tail = ListNode(None)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.size = 0
    
    def isEmpty(self):
        return self.size == 0

    def length(self):
        return self.size

    def addFirst(self, item):
        old_head = self.head.next

        old_head.pre = item
        item.next = old_head
        item.pre = self.head
        self.head.next = item

        self.size+=1

    def addLast(self, item):
        old_tail = self.tail.pre

        old_tail.next = item
        item.pre = old_tail
        item.next = self.tail
        self.tail.pre = item

        self.size+=1

    def removeFirst(self):
        if self.isEmpty():
            raise ValueError("Empty queue")

        temp = self.head.next
        self.head.next = temp.next
        temp.next.pre = self.head

        self.size-=1

        return temp

    def removeLast(self):
        if self.isEmpty():
            raise ValueError("Empty queue")
        
        temp = self.tail.pre
        self.tail.pre = temp.pre
        temp.pre.next = self.tail

        self.size-=1

        return temp