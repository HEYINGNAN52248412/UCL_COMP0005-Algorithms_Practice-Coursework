class ListNode():
    def __init__ (self, val):
        self.val = val
        self.next = None

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
            return
        
        curr = self.head
        while curr.next != self.head:
            curr=curr.next

        curr.next = item
        item.next = self.head

    def prepend(self, item):
        if self.isEmpty():
            self.head = item
            self.head.next = self.head
            return

        curr = self.head
        while curr.next != self.head:
            curr=curr.next
        
        curr.next = item
        item.next =self.head
        self.head = item
    
    def delete(self, pos):
        if self.isEmpty():
            raise ValueError("Empty List")

        if self.head.next == self.head:
            self.head = None
            return
        
        n = self.length()

        pos = pos%n

        if pos == 0:
            curr = self.head
            while curr.next != self.head:
                curr=curr.next
            
            curr.next = self.head.next
            self.head = curr.next
            return


        count = 0
        curr = self.head
        while count < pos-1:
            curr=curr.next
            count+=1
        curr.next = curr.next.next

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
        

        