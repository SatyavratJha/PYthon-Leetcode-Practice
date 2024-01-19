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

    
my_linked_list = LinkedList(4)
my_linked_list.append(2)
print("2 items in list")
my_linked_list.print_list()
my_linked_list.prepend(5)
print("3 items in list")
my_linked_list.print_list()

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
