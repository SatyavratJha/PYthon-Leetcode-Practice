def add_items(n):
    return n+n

add_items(10)
# In previous cases like O(n) or O(n^2), as n gets bigger number of operations gets bigger.
# In this case, if n is 1 or million, there will be only one operation "addtion", 
# Big(o) will be O(1), even if there is n+n+n instead of n+n, 
# O(n) is called contant time, meaning that as n increases the number of operations remanined same. Even we have 2 addtions instead of 1, the number of operations will remain constants as n increases. 
# O(1) if flat line across the bottom and just going to stay across the bottom as n increases, number of operations is not increasing.
# O(1) is the most effiecient Big(O)


# Anytime that we can make anything O(1) that is as optimal as we can make it.