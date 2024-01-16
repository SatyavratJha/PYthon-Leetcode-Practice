# class LinkedList:
    # def __init__(self, value):
    # Constructor is going to create a Node, its also going to initialize the new linked list
        
    # def append(self, value):
    # Create a new Node and add Node to end

    
    # def pop(self):
    # create new Node and add Node to beginning 

    
    # def prepend(self,value):
    # create new Node and insert that node at whatever index whereever we want that


    # def insert(self, index, value):

    # def remove(self,index):

# class Node:
    # def __init__(self, value):
    # this creates a new Node, whenever we want new node we will call for this class and this constructor which passes the value which we want to assign to new node.

    
    
    
# class LinkedList:
#     def __init__(self,value):
        
#     def append(self, value):
    
#     def pop(self):
    
#     def prepend(self,value):

#     def insert(self, index, value):

#     def remove(self,index):

# class Node:
#     def __init__(self,value):
#         self.value = value
#         self.next = None


def print_list(self):
    temp = self.head
    while temp is not None:
        print(temp.value)
        temp = temp.next


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

my_linked_list = LinkedList(4)

print(my_linked_list.head.value)

        