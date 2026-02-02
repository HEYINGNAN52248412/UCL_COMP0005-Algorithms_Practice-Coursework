class ListNode():
    def __init__ (self, val):
        self.val = val
        self.next = None
        self.pre = None

class CircularList():
    def __init__ (self):
        self.head = None
    
    def isEmpty (self):
        return self.head is None

    def length(self):
        if self.isEmpty():
            return 0
        if self.head.next == self.head:
            return 1

        count = 1
        curr = self.head
        while curr.next != self.head:
            curr=curr.next
            count+=1
        return count

    def append(self, item):
        if self.isEmpty():
            self.head = item
            self.head.next = self.head
            self.head.pre = self.head
            return
        
        curr = self.head.pre
        curr.next = item
        item.next = self.head
        item.pre = curr
        self.head.pre = item

    def prepend(self, item):
        self.append(item)
        self.head = self.head.pre

    def delete(self, pos):
        if self.isEmpty():
            raise ValueError("Empty List")

        if self.head.next == self.head:
            self.head = None
            return
        
        n = self.length()

        pos = pos%n

        if pos == 0:
            curr = self.head.pre
            #node-1 -> node1
            curr.next = self.head.next
            #node1 -> node-1
            self.head.next.pre = curr
            self.head = self.head.next
            return


        count = 0
        curr = self.head
        while count < pos-1:
            curr=curr.next
            count+=1
        curr.next = curr.next.next
        curr.next.pre = curr

    def access(self, pos):
        if self.isEmpty():
            raise ValueError("Empty List")
        
        n = self.length()
        pos = pos%n

        count = 0
        curr = self.head
        while count < pos:
            curr=curr.next
            count+=1
        return curr.val