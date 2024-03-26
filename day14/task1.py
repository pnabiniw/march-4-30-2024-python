# Create a decorator function which converts a string input to uppercase

def to_upper(func):
    def inner_fxn(*args, **kwargs):
        a = func(*args, **kwargs)
        return a.upper()
    return inner_fxn


@to_upper
def message(msg):
    return msg


result = message("Hello World")
print(result)  # HELLO WORLD
