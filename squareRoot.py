import math
print("Calculate the root of a number")

def square_root(number):
    if number < 0:
        return "You can't calculate the root of a negative"
    else:
        return math.sqrt(number)


number = float(input("Enter a number: "))

rootResult = square_root(number)

print(f"Result: {rootResult}")