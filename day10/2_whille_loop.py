# While loop is used with conditions or Truthy or Falsy values
# We should always update the condition variable from inside the while block.
# If the condition variable is not updated then the loop goes to infinite
# While loop runs until the condition is True

a = 0
while a <= 10:
    print(a)
    a += 1

while 3:  # This is an infinite loop
    print("Hello World")

# if we need infinite loop then:
while True:
    print("Hello World")
