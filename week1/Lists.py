#List operations

list2 = [1,3,5,2,5,2,56,86,346,856,34,7,36,86, 7, 23, 6]
list1 = []
for i in list2:
    if i%2:
        list1.append(i)

list2 = list1

list2 = sorted(list2, reverse=True)

list2.append(sum(list2))

print(list2)
