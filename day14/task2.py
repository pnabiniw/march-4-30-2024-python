# Create a decorator function "login_required" which asks for a password. If the password matches
# "1234" then allow permission to access the main function else display the message "Not Allowed !!"

def login_required(func):
    def inner_fxn(*args, **kwargs):
        pw = input("Enter your password ")
        if pw == "1234":
            return func(*args, **kwargs)
        else:
            return "Not Allowed !!"
    return inner_fxn


@login_required
def addition(a, b):
    return a + b


result = addition(3, 4)
print(result)
