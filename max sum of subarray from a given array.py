#problem: find the maximum value of a subarray from a given array



l = [1,2,3,4,3,2,1,4,8,10,2,-4]

ma = 0
su = 0
for i in range(0,len(l)-2):
    l1 = l[i:i+3]
    su = sum(l1)
    ma = max(ma,su)
print(ma)