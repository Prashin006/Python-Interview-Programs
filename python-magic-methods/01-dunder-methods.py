# Dunder / Magic methods
# Dunder stands for double underscore
# These are special / reserved methods in Python that map to some kind of behaviour
# __init__ is used to construct or create a new object
# Everything we create in Python is essentially an object

str1 = "hello"
str2 = "world"
def func():
    pass

new_str = str1.__add__(str2)
str1_len = str1.__len__()
print(type(func))
print(new_str)
print(str1_len)
