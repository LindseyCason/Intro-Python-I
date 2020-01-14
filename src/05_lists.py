# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE
x.append(4)
print(f"one ", x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE
print(f"two ",x + y)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
(x.extend(y))
x.pop(4)
print(f"three ", x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE
x.extend(y)
x.sort()
x.append(int(99))
x.append(int(10))
x.pop(6)
x.pop(7)
x.pop(6)
print(f"four", x)

# Print the length of list x
# YOUR CODE HERE
print(len(x))

# Print all the values in x multiplied by 1000
# YOUR CODE HERE

for i in x:
    print(i*1000)