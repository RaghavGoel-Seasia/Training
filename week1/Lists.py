#List operations

#Define a list
list2 = [1,3,5,2,5,2,56,86,346,856,34,7,36,86, 7, 23, 6]

#Create an empty list
list1 = []

#Iterate over original list
for i in list2:

    #If odd element
    if i%2:
        #Append to blank list
        list1.append(i)

#Overwrite original list with odd list
list2 = list1

#Sort list in reversed order
list2 = sorted(list2, reverse=True)

#Append the sum of the
list2.append(sum(list2))

print(list2)
