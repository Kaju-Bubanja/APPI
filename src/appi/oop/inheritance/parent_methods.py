class Parent:
    def foo(self):
        return "foo"

    def name(self):
        return "Parent"


class Child(Parent):

    def __init__(self, a, b):
        self.a = a
        self.b = b
    def name(self):
        return "Child"

    def parent_name(self):
        return super().name()

    def __str__(self):
        return f"a: {self.a}, b: {self.b}"


c = Child(42, "Hallo world")
print(c.foo())
print(c.name())
print(c.parent_name())
print(c)
