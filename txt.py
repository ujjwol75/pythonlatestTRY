rows = 6
current_number = 1
for i in range(1, rows):
    for j in range(-1+i, -1, -1):
        
        current_number =  2**j
        print(current_number, end=" ")
        
    
    print("")

