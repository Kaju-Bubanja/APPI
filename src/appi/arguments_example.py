def greet(answer_to_everything, *args, **kwargs):
    print(answer_to_everything)
    print(args)
    for key, value in kwargs.items():
        print(f"{key} => {value}")


greet(42, "*", ["wow", "mega"], user="Tom", city="London", pet=["Dog", "Cat", "Fish"])

