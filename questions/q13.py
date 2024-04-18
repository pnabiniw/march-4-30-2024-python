"""
Explain method overloading and overriding in python
"""
class A:
    def description(self):
        return "Hello"


class B(A):

    def description(self):
        print(super().description())
        return "Python"
