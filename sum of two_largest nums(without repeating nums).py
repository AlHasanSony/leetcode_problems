#problem: Given a list of numbers, return the sum of the two largest numbers.
# it can remove the repeated numbers from the list.



a = [1, 2, 5, 2, 7, 3, 9, 5, 7, 9]
a = set(a) 
max1 = max(a) # largest
a = list(a) # convert back to list
a.pop(a.index(max1)) # remove largest
max2 = max(a) # second largest
print(max1 + max2) # sum

