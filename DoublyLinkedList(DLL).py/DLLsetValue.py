class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None

class DoublyLinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next
    def append(self,value):
        new_node = Node(value)
        # if self.length == 0:
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev=self.tail
            self.tail = new_node
        self.length+=1
        return True
    # MINE
    # def pop(self):
    #     if self.head is None:
    #         return None
    #     else:
    #         temp2 = self.tail
    #         temp = self.tail.prev
    #         self.tail.prev = None
    #         self.tail = temp
    #         self.tail.next = None
    #         self.length-=1
    #         return temp2
    
    # def pop(self):
    #     if self.length == 0:
    #         return None
    #     temp = self.tail
    #     self.tail = self.tail.prev
    #     self.tail.next = None
    #     temp.prev = None
    #     self.length -=1
    #     if self.length == 0:
    #         self.head = None
    #         self.tail = None
    #     return temp 
    
    # Much easier to read
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else: 
            # only extra line added.
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -=1
        return temp
    #Mine is also correct giving same output just sequence is change

    # def prepend(self,value):
    #     new_node = Node(value)
    #     if(self.length==0):
    #         self.head=new_node
    #         self.tail=new_node
    #     self.head.prev=new_node
    #     new_node.next=self.head
    #     self.head=new_node
    #     self.length+=1
        
    def prepend(self,value):
        new_node = Node(value)
        if(self.length==0):
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
        self.length+=1
        return True
    
    # Mine is same as the instructer Correct Good Job
    def popFirst(self):
        if(self.length==0):
            return None
        temp=self.head
        if(self.length==1):
            self.head=None
            self.tail=None
        else:
            self.head=self.head.next
            self.head.prev = None
            temp.next= None
        return temp
    # Mine
    def get(self,index):
        if self.length == 0 or index < 0 or index >=self.length:
            return False
        else:
            temp = self.head
            for _ in range(index):
                temp=temp.next
            return temp
    # Lecturer optimized for DLL to go through tail if it is near tail
    def get(self,index):
        if self.length == 0 or index < 0 or index >=self.length:
            return False
        temp = self.head
        if index < self.length /2:
            for _ in range(index):
                temp=temp.next
        else:
            temp = self.tail
            for _ in range (self.length-1, index, -1):
                temp=temp.prev
        return temp
    # Mine
    # def set_Value(self,index,value):
    #     if index < 0 or index > self.length:
    #         return False
    #     # if index == 0:
    #     #     return self.prepend(value)
    #     # if index == self.length:
    #     #     return self.append(value)
    #     temp = self.get(index)
    #     if temp: 
    #         temp.value = value
    #     return temp
    # Lecturer's    
    def set_Value(self,index,value):
        temp = self.get(index)
        if temp: 
            temp.value =  value
            return True
        return False
       


        



my_doubly_linked_list = DoublyLinkedList(10)
my_doubly_linked_list.print_list()
print("after append")
my_doubly_linked_list.append(5)
my_doubly_linked_list.print_list()
# print("after pop")
# my_doubly_linked_list.pop()
# my_doubly_linked_list.print_list()
print("after prepend")
my_doubly_linked_list.prepend(50)
my_doubly_linked_list.print_list()
# print("after First")
# my_doubly_linked_list.popFirst()
# my_doubly_linked_list.print_list()
print("after get ->")
print(my_doubly_linked_list.get(0),'\n \n ')
my_doubly_linked_list.print_list()
print("after set ->")
print(my_doubly_linked_list.set_Value(2,23),'\n \n ')
my_doubly_linked_list.print_list()

