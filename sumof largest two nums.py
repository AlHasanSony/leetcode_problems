#problem: Given a list of numbers, return the sum of the two largest numbers.
# it can't remove the repeated numbers from the list.


x = [1, 2, 5, 2, 7, 3, 9, 5, 9]
max1 = 0;
max2 = 0;
for i in range(len(x)):
    if x[i] > max1:
        max2 = max1
        max1 = x[i]
    elif x[i] > max2:
        max2 = x[i]

print(max1+max2)