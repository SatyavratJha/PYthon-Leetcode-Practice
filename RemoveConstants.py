def print_items(n):
    for i in range(n):
        print(i)
    for j in range(n):
        print(j)

print_items(10)
#This run n+n times or 2n, O(2n) = O(n), we dropped 2