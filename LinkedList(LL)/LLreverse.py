class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def append(self, value):
        new_node=Node(value)
        # if(self.head is None):
        if(self.length == 0):
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1
        return True
    
    def prepend(self, value):
        new_node=Node(value)
        # if(self.head is None):
        if(self.length == 0):
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next=self.head
            # self.head.next = new_node
            self.head = new_node
        self.length +=1
        return True
    def pop(self):
        # if(self.head is None):
        if(self.length == 0):
            return None
        pre = self.head
        temp = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next=None

        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value
            # while(self.head is not None):
            #     self.head = self.next
    def popFirst(self):
        # if(self.head is None):
        if(self.length == 0):
            return None
        temp = self.head
        # while temp.next:
        #     pre = temp
        #     temp = temp.next
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp.value

    def get(self,index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp=temp.next
        return temp

    def set_value(self, index,value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    def insert(self,index,value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node=Node(value)
        temp = self.get(index-1)
        new_node.next=temp.next
        temp.next = new_node
        self.length+=1
        return True
    def remove(self,index):
        if index < 0 or index >=self.length:
            return None
        if index == 0:
            return self.popFirst()
        if index == self.length-1:
            return self.pop()
        prev = self.get(index-1)
        temp = prev.next
        prev.next=temp.next
        temp.next=None
        self.length-=1
        return temp
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after=temp.next
            temp.next=before
            before=temp
            temp=after


        



my_linked_list = LinkedList(4)
my_linked_list.append(2)
print("2 items in list")
my_linked_list.print_list()
my_linked_list.prepend(5)
print("3 items in list")
my_linked_list.print_list()
my_linked_list.append(9)
print("4 items in list")
my_linked_list.print_list()
my_linked_list.append(8)
print("5 items in list")
my_linked_list.print_list()
print("get item through get method in list:::-->>> \n")
print(my_linked_list.get(0), '\n')
print("set Item \n")
print(my_linked_list.set_value(2,10), '\n')
my_linked_list.print_list()

print("insert Item \n")
print(my_linked_list.insert(3,23), '\n')
my_linked_list.print_list()

print("remove Item \n")
print(my_linked_list.remove(4), '\n')
my_linked_list.print_list()
print("reversed linked list  \n")
my_linked_list.reverse()
my_linked_list.print_list()


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
