# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(x):
    if x%2 == 0:
        return(f"True")
    elif x%2 !=0:
        return(f"False")
# Read a number from the keyboard
num = input("Enter a number: ")
x = int(num)
print(is_even(x))

# Print out "Even!" if the number is even. Otherwise print "Odd"
result = is_even(x)
if result == "True":
        print("Even")
else:
        print("Odd")


