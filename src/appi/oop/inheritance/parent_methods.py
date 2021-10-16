class Parent:
    def foo(self):
        return "foo"

    def name(self):
        return "Parent"


class Child(Parent):
    def name(self):
        return "Child"

    def parent_name(self):
        return super().name()

    def __str__(self):
        return "Super nicely formatted name"


c = Child()
print(c.foo())
print(c.name())
print(c.parent_name())
print(c)
