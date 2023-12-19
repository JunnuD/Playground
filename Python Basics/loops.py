for num in [1, 2, 3, 4, 5]:
   print(num)
    

for i in range(6):
    print(i)
    
print()
    
i = 0
while i<=5:
   print(i)
   i += 1
   
   
# Using both for-loop and while-loop

# For-loop to iterate over a list
for i in range(1, 6): 
    print("For-loop iteration:", i)
    if i == 5:
       print("End!")

# While-loop to count down
count = 5
while count > 0:
    print("While-loop countdown:", count)
    count -= 1
    if count == 0:
       print("End!")
