def max_magnitude(num_1, num_2, num_3):
    max_mag = max(abs(num_1), abs(num_2), abs(num_3))
    
    if max_mag == abs(num_1):
        return num_1
    elif max_mag == abs(num_2):
        return num_2
    else:
        return num_3


num_1 = int(input())
num_2 = int(input())
num_3 = int(input())
result = max_magnitude(num_1, num_2, num_3)
print(result)
