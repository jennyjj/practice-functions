"""
Complete the code to pass all the test
"""


def greet_user():
    """Prints out each item in a list.

    >>> greet_user()
    Welcome
    """
    print "Welcome"

def avg_numbers(num1, num2):
    """Adds two numbers together and divides sum by 2

    >>> avg_numbers(2, 10)
    6.0
    >>> avg_numbers(3, 10)
    6.5
    """

    # ADD YOUR CODE HERE
    average = (float(num1) + float(num2)) / 2
    return average

def print_list(lst):
    """Prints out each item in a list.

    >>> print_list(["ant", "bee", "caterpillar"])
    ant
    bee
    caterpillar
    """

    # ADD YOUR CODE HERE
    for item in lst:
        print item

def calculate_total_bill(bill, tip):
    """Calculates the total bill with tip

    Multiply the tip and bill and that sum is added to the bill.

    >>> calculate_total_bill(100, .20)
    120.0
    >>> calculate_total_bill(200, .25)
    250.0
    """

    # ADD YOUR CODE HERE
    tip = bill * tip
    total_bill = bill + tip
    return total_bill



#####################################################################
# Please don't touch the code below!
# This allows us to run the doctests
if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. AWESOME WORK!\n"
