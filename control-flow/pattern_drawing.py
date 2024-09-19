size = int(input("enter the size of the pattern: "))

if size <= 0:
    print("please enter a positive number ")
else:    
    row = 0
    while row < size:
       for _ in range(size):
          print("*", end="")
       print()
       row +=1