#problem: Given a list of numbers, return the sum of the two largest numbers.

# BUt it can't remove the repeated numbers from the list.



#initialize these to huge negative numbers
largest = 0
second_largest = 0
l = [9,9,1,3,4,5,7,0]
for item in l:
    if item > largest:
        second_largest = largest
        largest = item
    elif item > second_largest:
        second_largest = item

print(largest+second_largest)
# 17