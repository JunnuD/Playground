# Question, 

# Move the zeros to the end of the list

list = [1, 0, 4, 7, 0, 9]

for item in list:
    if item == 0:
        list.remove(item)
        list.append(item)

print(list)
