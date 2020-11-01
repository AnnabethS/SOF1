data = [[1,2,3], [2], [1, 2, 3, 4]] 

def sum_lists(list_2D):
    output = [] 
    total = 0 
    for row in data:     
        for val in row:         
            total += val         
        output.append(total)
        total = 0 
    return output

print(sum_lists(data))            