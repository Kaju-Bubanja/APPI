import operator
from log_handling import setup_logger, close_log_handlers

# Make a simple calculator, where the user is repeatedly asked to enter numbers and operands and the calulator
# returns  the result,
# until the user enters 'exit'. The calculator should also log all the data inputted and any exceptions which might
# happen  e.g. DivisonByZero, NotANumber
# and still continue to function even though an exception happened
# Catch at least 3 specific exceptions and log a sensible message
# Allow the user to use the last result by typing "last" instead of a number as an input
# You can use following dictionary to retrieve operators and use the operator like so operator.add(x, y)
# example how to catch an Exception
try:
    int("abc")
except ValueError:
    print("Can't convert to number")
# print(2+2) == print(operator.add(2, 2))
ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "**": operator.pow,
    "/": operator.truediv,
    "%": operator.mod,
}

# Write your solution below
