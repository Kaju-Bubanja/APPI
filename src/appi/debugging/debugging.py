x = "Hallo world"
print(x)
sum = 0
for x in range(10):
    sum += x
    print(x)

print(sum)


def average(a, b):
    return a + b / 2


def average2(a, b):
    result = a + b / 2
    return result


average(10, 20)
average2(10, 20)

10/0


def get_discount(price):
    price = price*1.9
    return price


def get_item_price(price, amount):
    if amount > 10:
        price = get_discount(price)
    result = price*amount
    print(result)
    return result


get_item_price(10, 5)
get_item_price(10, 7)
get_item_price(10, 20)
