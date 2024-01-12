def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j) # nested loops ran O(n^2) times
    for k in range(n):
        print(k)       # single loop ran O(n) times

     

print_items(10)
#Total number of items we output was O(n^2) + O(n) = O(n^2 +n), so in percentage view when we deal with n as millions or billions,  n^2 will be dominant as compared to n which will be non-dominant, so it will be dropped
#So Big(O) will be O(n^2)