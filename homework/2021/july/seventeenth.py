x = int(input("enter num"))
y = int(input("enter num"))


class Parent:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_value(self):
        print(self.a ** self.b)


class Child(Parent):
    def get_value(self):
        super().get_value()  # super(Child, self).get_value()
        num = 1
        for integer in range(1, self.a + 1):
            num *= integer
        print(num)


child = Child(x, y)
child.get_value()
