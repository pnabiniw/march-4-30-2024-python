# Advantage of using context manager in file is, we do not need to explicitly close the file
# the file closes itself while the context manager block ends


filename = "test1.txt"

with open(filename, "w") as fp:  # context manager
    fp.write("Writing in file using context manager")


with open(filename, "r") as fp:
    data = fp.read()
print(data)


with open(filename, "r+") as fp:
    data = fp.read()
    fp.write("Content from r+ mode")
print(data)


with open(filename, "w+") as fp:
    fp.write("Content from w+")
    fp.seek(0)
    data = fp.read()
print(data)
