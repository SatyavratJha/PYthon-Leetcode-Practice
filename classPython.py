class Cookie:
    def __init__(self,color):
        self.color =color
    def get_color(self):
        return self.color
    def set_color(self,color):
        self.color=color

cookie_one = Cookie('green')
cookie_two = Cookie('yellow')

print(cookie_one.color)
print(cookie_two.color)

cookie_three = Cookie('blue')
cookie_four = Cookie('red')
print('Cookie three is', cookie_three.get_color())
print('Cookie four is', cookie_four.get_color())

cookie_four.set_color('pink')
print('\n Cookie three is still', cookie_three.get_color())
print('Cookie four is now', cookie_four.get_color())

# How are we going to use class to define every data structure

# class LinkedList:
#     def __init__(self,value):
        
#     def append(self, value):
    
#     def pop(self):
    
#     def prepend(self,value):

#     def insert(self, index, value):

#     def remove(self,index):




