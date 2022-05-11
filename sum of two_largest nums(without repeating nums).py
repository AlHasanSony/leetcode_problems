#problem: Given a list of numbers, return the sum of the two largest numbers.
# it can remove the repeated numbers from the list.


array = [1, 2, 5, 2, 7, 3, 9, 5, 7, 9]

array = set(array) 
#set is used to remove the repeated numbers from the list

max1 = max(array) # largest
array = list(array) # convert back to list
array.pop(array.index(max1)) # remove largest
max2 = max(array) # second largest
print(max1 + max2) # sum


#output: 16