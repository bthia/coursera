print("\n\nZip Example 1 ******")

L1 = [1, 5, 12, 90, 232]
L2 = [4, 9, 2, 19, 29]

L3 = [x1+x2 for (x1, x2) in list(zip(L1, L2))]

print(L1)
print(L2)
print(L3)


print("\nZip Example 2 - with Map ******")


L1 = [5, 24, 53, 113, 944]
L2 = [4, 35, 23, 291, 423]

L3 = list(map(lambda x: x[0]+x[1], zip(L1, L2)))

print(L1)
print(L2)
print(L3)


print('\nExample 3 - with list comprehension ***************')
L1 = [1, 5, 2, 16, 32, 3, 54, 8, 100]

L2 = [1, 3, 10, 2, 42, 2, 3, 4, 3]

L3 = [x1 + x2 for (x1, x2) in zip(L1, L2) if x1>10 and x2<5]

print(L1)
print(L2)
print(L3)