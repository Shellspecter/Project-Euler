#Project Euler 1

#Add all the natural numbers below one thousand 
#that are multiples of 3 or 5.

numbers = []

for i in range(3, 1000):
    if i%3 == 0:
        numbers.append(i)

    elif i%5 == 0:
        numbers.append(i)

number = sum(numbers)

print number
