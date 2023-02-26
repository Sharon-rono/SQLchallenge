#Given an array of integers, find the sum of its elements

ar = [1,2,3]

def add(ar):
    sum = 0
    for i in ar:
        sum += i
    return sum
print(add(ar))
