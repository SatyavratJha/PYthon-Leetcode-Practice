def print_items(a,b):
    for i in range(a):
        print(i)
    for j in range(b):
        print(j)
print_items(10) 
# Big(O) will be O(a+b)
def print_items1(a,b):
    for i in range(n):
        for j in range(n):
            print(a," ",b)
print_items1(20,30)
#Big(O) wil be O(a*b)