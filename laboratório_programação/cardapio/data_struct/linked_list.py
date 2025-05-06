class Node():
    def __init__(self,value:"anything",prev:"Node",next:"Node"):
        self.value=value
        self.next=next
        self.prev=prev
    

class Linked_List():
    def __init__(self):
        self.head=Node(None,None,None)
        self.init=self.head
        self.last=self.head


    def remove(self):
        if self.head.value==None:
            if not self.head.prev:
                self.init=self.head
                self.head.prev=Node(None,None,self.head)
            if not self.head.next:
                self.last=self.head
                self.head.next=Node(None,self.head,None)
            return
        temp=self.head.prev
        if not temp:
            temp=Node(None,None,None)
        self.head=self.head.next
        if not self.head:
            self.head=Node(None,None,None)
        temp.next=self.head
        self.head.prev=temp
        self.head=self.head.prev
        
        if not self.head.prev:
            self.init=self.head
            self.head.prev=Node(None,None,self.head)
        if not self.head.next:
            self.last=self.head
            self.head.next=Node(None,self.head,None)
    def remove_at_index(self,index:int):
        for i in range(index):
            if not self.head.next:
                break
            self.forward()
        if index<0:
            self.head.go_last()
        self.remove()
        self.go_init()

        if self.head.prev.value == None:
            self.init=self.head
        if self.head.next.value == None:
            self.last=self.head


    def insert(self,value:"anything"):
        if self.head.value == None:
            self.head.value=value
            if not self.head.prev:
                self.head.prev=Node(None,None,self.head)
            if not self.head.next:
                self.head.next=Node(None,self.head,None)
            return
        temp=self.head.prev
        if not temp:
            temp=Node(None,None,None)
        temp.next=Node(value,temp,self.head)
        temp=temp.next
        self.head.prev=temp
        self.head=self.head.prev
        
        if not self.head.prev:
            self.init=self.head
            self.head.prev=Node(None,None,self.head)
        if not self.head.next:
            self.last=self.head
            self.head.next=Node(None,self.head,None)
    def insert_at_index(self,value:"anything",index:int):
        for i in range(index):
            if not self.head.next:
                break
            self.head=self.head.next
        if index < 0:
            self.go_last()
            self.forward()
        self.insert(value)

        if self.head.prev.value == None:
            self.init=self.head
        if self.head.next.value == None:
            self.last=self.head

    def forward(self):
        if self.head.next == None:
            return
        self.head=self.head.next
    def backward(self):
        if self.head.prev == None:
            return
        self.head=self.head.prev

    def in_end(self):
        return self.head==self.last
    def in_start(self):
        return self.head==self.init
    def go_init(self):
        self.head=self.init
    def go_last(self):
        self.head=self.last

    def display(self):
        temp=self.init
        while temp!=self.last:
            temp=temp.next
            print(temp.value,end=' ')

if __name__ == "__main__":
    tst=Linked_List()
    tst.insert_at_index(1,0)
    tst.insert_at_index(2,0)
    tst.insert_at_index(3,0)
    tst.display()
    tst.remove_at_index(0)
    print()
    tst.display()
