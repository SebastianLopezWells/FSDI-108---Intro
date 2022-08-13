# imports

# global variables
from site import addpackage


prices = [123, 1, 32, 6453, 12, 457, 879, 65, 89, 0, 0, 1, 234, 1, 8, 9187, 1, 0]
# functions
def sum_all(numbers):
    sum = 0
    for price in numbers:
        sum += price
    print("The result is" + str(sum))


def count_all_lower_50(numbers):
    for price in numbers:
        if price < 50:
            print(str(price) + " Is lower then 50")


def print_some_nums():
    for i in range(0, 10):
        print(i)


def list_test():
    names = []

    # add
    names.append("jorge")
    names.append("Sebastian")
    names.append("Jose")

    # get at index
    print(names[0])
    print(names[-1])  # last of the list


def sum(n1, n2):
    res = int(n1) + int(n2)
    print(res)


def div(n1, n2):
    if n2 == 0:
        print("Division by zero is not possible")
    else:
        res = float(n1) / float(n2)
        print("The result is" + str(res))


# plain instructions
print("Starting Example 1")
# count_all_lower_50(prices)
#
# num1 = input("Please enter a numbers")
# num2 = input("Please enter a numbers")
# sum(num1, num2)

num3 = input("Please enter a numbers ")
num4 = input("Please enter a numbers ")
div(num3, num4)
