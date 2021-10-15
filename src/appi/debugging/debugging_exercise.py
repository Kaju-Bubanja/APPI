import operator
from log_handling import setup_logger, close_log_handlers

# Make a simple calculator, where the user is repeatedly asked to enter numbers and operands and the calulator returns the result,
# until the user enters 'exit'. The calulator should also log all the data inputed and any exceptions which might happen e.g. DivisonByZero, NotANumber
# and still continue to function even though an exception happened
# Catch 3 specific exceptions and log a sensible message
# You can use following dictionary to retrieve operators and use the like operator.add(x, y)
ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "**": operator.pow,
    "/": operator.truediv,
    "%": operator.mod,
}

# Write your solution below
