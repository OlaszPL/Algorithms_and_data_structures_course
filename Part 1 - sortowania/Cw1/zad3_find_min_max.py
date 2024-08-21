# znalezienie najmiejszego i największego elementu w tablicy przy tylko n porównań

def min_max(T):
    n = len(T)
    min = T[-1] # bo dla nieparzystej tablicy nie rozpatrzy ostatniego elementu
    max = T[-1]

    for i in range(0, n - 1, 2): # robimy tylko 1,5n
        if T[i] < T[i + 1]:
            if T[i] < min:
                min = T[i]
            
            if T[i + 1] > max:
                max = T[i + 1]   
        else:
            if T[i + 1] < min:
                min = T[i + 1]
            
            if T[i] > max:
                max = T[i]
    
    return min, max

T = [23, 1, 45, 67, 12, -89, -97, 140, 45, 112, 7, 23, -5]
print(min_max(T))