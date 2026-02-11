l1 = [3,4,6,23,78,13]
b = 1
c = len(l1)
while b < c:
    if l1[b] < l1[b-1]:
        l1[b], l1[b-1] = l1[b-1], l1[b]
        b = 0
    b += 1
# print(l1)
print([l1[0], l1[-1]] )
