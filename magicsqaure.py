def magic_square(matrix):
    iSize = len(matrix[0])
    sum_list = []
    
    #Vertical:
    for col in range(iSize):
        sum_list.append(sum(row[col] for row in matrix))
    
    #Horizontal
    sum_list.extend([sum (lines) for lines in matrix])
    
    #Diagonals
    dlResult = 0
    for i in range(0,iSize):
        dlResult +=matrix[i][i]
    sum_list.append(dlResult)  
    
    drResult = 0
    for i in range(iSize-1,-1,-1):
        drResult +=matrix[i][i]
    sum_list.append(drResult)
 
    if len(set(sum_list))>1:
        return False
    return True
print(magic_square([[16, 23, 17], [78, 32, 21], [17, 16, 15]]))
print(magic_square([[23, 28, 21], [22, 24, 26], [27, 20, 25]]))