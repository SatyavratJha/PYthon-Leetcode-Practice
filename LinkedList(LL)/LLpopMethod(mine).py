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
#Mine Pop
    def pop(self):
        # if(self.head is None):
        if(self.length == 0):
            return False
        else:
            if self.length == 1:
                self.head.next = None
                self.head = None
            else:
                if self.length > 1:
                    i = self.length
                    while( i > 1):
                        self.head = self.head.next
                        i -= 1
                    if i == 1:
                        self.tail.next= self.head
                        self.tail = None

            self.length -= 1
            return True
            # while(self.head is not None):
            #     self.head = self.next

my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.print_list()
# print(my_linked_list.head.value)