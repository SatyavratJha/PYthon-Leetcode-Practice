def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i," ",j)

     

print_items(10)
#This run n*n times or n^2 O(n^2). Line for O(n^2) is much steeper than O(n) in graph, that means it lot efficient from time complexity stand point.