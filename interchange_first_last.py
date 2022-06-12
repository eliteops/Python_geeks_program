arr = list(map(int, input().split()))                # Used to take multiple inputs in list 
a, *b, c = arr                                       #  *b works as a keeper to handle more values 
arr = c, *b, a
print(arr)
