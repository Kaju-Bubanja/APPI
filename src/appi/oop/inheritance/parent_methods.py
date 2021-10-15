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


c = Child()
print(c.foo())
print(c.name())
print(c.parent_name())
