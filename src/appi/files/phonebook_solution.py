import json
import pickle


def main():
    serializer_name = "json"
    # serializer_name = "pickle"
    if serializer_name == "json":
        serializer = json
        file_mode_addition = ""
    elif serializer_name == "pickle":
        serializer = pickle
        file_mode_addition = "b"
    else:
        print("Selected unknown serializer. Exiting")
        return
    mode = input("Enter 's' search mode and 'i' for input mode")
    if mode == "s":
        # When using pickle the file ending should be .pickle, but to be able to switch easily we just leave it .json
        with open(f"address_book.{serializer_name}", "r" + file_mode_addition) as file:
            address_book_dict = serializer.load(file)
        while True:
            name = input("Input name")
            if name == "exit":
                break
            try:
                print(address_book_dict[name])
            except KeyError:
                print(f"The user {name} doesn't exist")
    elif mode == "i":
        name_number = {}
        while True:
            name = input("Input name")
            if name == "exit":
                break
            number = input("Input phone number")
            name_number[name] = number
        with open(f"address_book.{serializer_name}", "w" + file_mode_addition) as file:
            serializer.dump(name_number, file)
        print(name_number)
    else:
        print("Invalid mode selected closing application")


if __name__ == '__main__':
    main()
