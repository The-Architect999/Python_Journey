def highest_even(a):
    even = []
    highest = 0
    for numbers in a:
        if numbers % 2 == 0:
            even.append(numbers)
    for nos in even:
        if (nos - highest) > 0:
            highest = (nos)
    return(highest)
    
print(highest_even([10,2,3,4,8,11]))
