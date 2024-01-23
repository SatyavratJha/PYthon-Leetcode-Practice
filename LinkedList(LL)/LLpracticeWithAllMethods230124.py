class Node:
## constructer method
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
## constructer method
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1
## print list 1
    def print_list(self):
        temp=self.head
        for _ in range(self.length):
            if temp:
                print(temp.value)
            temp=temp.next
## append
    def append(self,value):
        new_node=Node(value)
        if(self.length==0):
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next = new_node
            self.tail=new_node
        self.length+=1
        return True
## pop
    def pop(self):
        if(self.length==0):
            return None
        if(self.length==1):
            self.head=None
            self.tail=None
        temp=self.head
        temp2 = self.tail
        for _ in range(self.length-1):
            temp=temp.next
        temp.next=None
        self.tail=temp
        self.length-=1
        return temp2
## prepend
    def prepend(self,value):
        new_node=Node(value)
        if(self.length==0):
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.length+=1
        return True
## pop first
    def popFirst(self):
        if(self.length==0):
            return None
        if self.length == 1:
            self.head=None
            self.tail=None
        temp=self.head
        self.head=self.head.next
        temp.next=None
        self.length-=1
        return temp
## get
    def get(self,index):
        if index < 0 or index >= self.length:
            return False
        temp = self.head
        for _ in range(i):
            temp=temp.next
        return temp
## set
    def set(self,index,value):
        if index < 0 or index >= self.length:
            return False
        temp=self.head
        for _ in range(index):
            temp=temp.next
        temp.value=value
        return True
## insert
    def insert(self,index,value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node=Node(value)
        temp=self.head
        for _ in range(index):
            temp=temp.next
        new_node.next=temp.next
        temp.next=new_node
        self.length+=1
        return True
## remove
    def remove(self,index):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.popFirst()
        if index == self.length:
            return self.pop()
        temp=self.head
        for _ in range(index-1):
            temp=temp.next
        prev = temp.next
        temp.next=prev.next
        prev.next=None
        self.length+=1
        return True
## reverse
    def reverse(self):
        if(self.length==0):
            return False
        else:
            after=self.head
            before=None
            temp=self.head
            self.tail=after
            for _ in range(self.length):
                temp=after.next
                after.next=before
                before=after
                after=temp
                temp=temp.next
        return True        
            

## should be done in 60 min max on my own, practice daily till i can do in 30 min, 15 min




# my_linked_list = LinkedList(4)
# my_linked_list.append(2)
# print("2 items in list")
# my_linked_list.print_list()
# my_linked_list.prepend(5)
# print("3 items in list")
# my_linked_list.print_list()
# my_linked_list.append(9)
# print("4 items in list")
# my_linked_list.print_list()
# my_linked_list.append(8)
# print("5 items in list")
# my_linked_list.print_list()
# print("get item through get method in list:::-->>> \n")
# print(my_linked_list.get(0), '\n')
# print("set Item \n")
# print(my_linked_list.set_value(2,10), '\n')
# my_linked_list.print_list()

# print("insert Item \n")
# print(my_linked_list.insert(3,23), '\n')
# my_linked_list.print_list()

# print("remove Item \n")
# print(my_linked_list.remove(4), '\n')
# my_linked_list.print_list()
# print("reversed linked list  \n")
# my_linked_list.reverse()
# my_linked_list.print_list()


# print("2 items in list after popFirst")
# my_linked_list.popFirst()
# my_linked_list.print_list()

# print("pop once")
# print(my_linked_list.pop())
# my_linked_list.print_list()
# print("pop twice")
# print(my_linked_list.pop())
# my_linked_list.print_list()
# print("pop thrice")
# print(my_linked_list.pop())
# my_linked_list.print_list()

# print(my_linked_list.head.value)
