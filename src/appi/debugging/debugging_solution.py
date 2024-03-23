import operator
import time
from log_handling import setup_logger, close_log_handlers

# Make a simple calculator, where the user is repeatedly asked to enter numbers and operands and the calulator
# returns  the result,
# until the user enters 'exit'. The calculator should also log all the data inputted and any exceptions which might
# happen  e.g. DivisonByZero, NotANumber
# and still continue to function even though an exception happened
# Catch at least 3 specific exceptions and log a sensible message
# Allow the user to use the last result by typing "last" instead of a number as an input
# You can use following dictionary to retrieve operators and use the operator like so operator.add(x, y)
ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "**": operator.pow,
    "/": operator.truediv,
    "%": operator.mod,
}


# Write your solution below
def main():
    log = setup_logger("calculator.log")
    log.info("Welcome to the simple python calculator")
    log.info("Enter exit at any time to exit the calculator")
    log.info("Type last to use the last result instead of an operand")
    while True:
        try:
            # Sleep a bit to let the welcome message and the result message reach the outputstream first
            time.sleep(0.1)
            x = input("Enter a first operand")
            if x == "exit":
                break
            elif x == "last":
                x = result
            else:
                x = float(x)
            inputed_operator = input(f"Enter an operator. Valid options are {list(ops.keys())}")
            if inputed_operator == "exit":
                break
            operation = ops[inputed_operator]
            y = input("Enter a second operand")
            if y == "exit":
                break
            elif y == "last":
                y = result
            else:
                y = float(y)
            result = operation(x, y)
            log.info(f"{x} {inputed_operator} {y} = {result}")
        except ValueError as e:
            log.debug(e)
            log.warning("Couldn't convert input to number")
        except KeyError as e:
            log.warning("Didn't recognize operator")
        except ZeroDivisionError:
            log.warning("Can't divide by zero")
        except NameError as e:
            log.warning("Calculator just started and doesn't have a last result")
        except Exception as e:
            log.exception("An unexpected exception happened. Stacktrace follows")
    log.info("Shutting down python calculator")
    close_log_handlers(log)


if __name__ == '__main__':
    main()
