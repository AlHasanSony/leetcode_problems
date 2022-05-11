#problem: Given a list of numbers, return the sum of the two largest numbers.
# but it can't remove the repeated numbers from the list.

l = [1, 2, 5, 2, 7, 3, 9, 5]

# find largest
largest = max(l)
# remove from list
l.remove(largest)
# second largest
largest2 = max(l)
# remove from list
l.remove(largest2)
print(largest+largest2)



# l = [1, 2, 5, 2, 7, 3, 9, 5]
# l.pop(l.index(max(l))) + l.pop(l.index(max(l)))
# print(largest+largest2)