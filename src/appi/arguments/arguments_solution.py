# Write a function which takes any amount of arguments and named arguments and concatenates all the strings it finds and
# sums all the numbers it finds and returns both results
# Hint: Use type(object) to find the type of an object

def foo(*args, **kwargs):
    result_string = ""
    result_sum = 0
    for arg in args:
        if type(arg) == str:
            result_string += arg
        elif type(arg) == float or type(arg) == int:
            result_sum += arg
        else:
            print(arg, "Argument is neither str nor float. Skipping it")
    for arg in kwargs.values():
        if type(arg) == str:
            result_string += arg
        elif type(arg) == float or type(arg) == int:
            result_sum += arg
        else:
            print(arg, "Argument is neither str nor float. Skipping it")
    return result_string, result_sum


print(foo("Hallo ", "World", 42, 10, ["Wow", 3.141], first=" Zürich", second=18, special_arg=["Special Wow", 3], last=0.333))
