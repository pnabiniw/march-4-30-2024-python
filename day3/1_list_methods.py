# March 10

# sort() and reverse()


a = [5, 1, 3, 10, 12, 4]
a.sort()  # ascending order sort
print(a.sort())  # None
print(a)

a = ["banana", "apple", "orange"]
a.sort()
print(a)

a.sort(reverse=True)  # descending order sort
print(a)


# reverse()
a = [5, 1, 3, 10, 12, 4]
a.reverse()
print(a)  # [4, 12, 10, 3, 1, 5]


def addition(a, b):
    return a + b


result = addition(2, 3)
print(result)
