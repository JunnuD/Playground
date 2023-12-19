""""
Fizz Buzz
print 1-100...
 if number divisible by 3 print Fizz
 if number divisible by 5 print Buzz
 if both 3 and 5 print FizzBuzz
 
 if divisible by 7 print Guzz
 
 How about count the number of "FizzBuzzGuzz"?

"""

count_FizzBuzzGuzz = 0

for i in range(1, 1010):
    
    if i % 3 == 0 and i % 5 == 0 and i % 7 == 0:
        print("FizzBuzzGuzz")
        count_FizzBuzzGuzz += 1
    elif i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0 and i % 7 == 0:
        print("FizzGuzz")
    elif i % 5 == 0 and i % 7 == 0:
        print("BuzzGuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 7 == 0:
        print("Guzz")
    else:
        print(i)
        
count_FizzBuzzGuzz
print("FizzBuzzGuzz was printed out: ", count_FizzBuzzGuzz, " times.")
