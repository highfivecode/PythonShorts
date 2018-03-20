"""
HighFiveCode - https://highfivecode.com/
HFC YouTube Channel: https://www.youtube.com/channel/UCOmiui0ghT5OoVdD1wi4mFA
Send requests to: https://highfivecode.com/suggestions/

a == b evaluates if the VALUES of a and b are the same (value equality)
a is b evualuates if the OBJECTS a and b are the same (reference equality)
"a != b" and "a is not b" do the opposite of the above

Quick Gotcha:
Python caches integers in the range of [-5, 256]
so given:
a = 256
b = 256
a == b # True, the VALUES (256) of a and b are the same
a is b # True, the OBJECTS (a and b) point to same spot in memory, because of caching
a = 257
b = 257
a == b # True, the VALUES (256) of a and b are the same
a is b # False, the OBJECTS (a and b) are now different, they are not cached
"""

# Uncomment this code and Copy this code into the python interpreter
# a = 1024
# b = 1024
# a == b # returns true, same value
# a is b # returns false, different objects
# hex(id(a)) #prints the hex memory address where a is stored
# hex(id(b)) #prints the hex memory address where b is stored
#
# a = "hello world"
# b = "hello world"
# a == b # true
# a is b # false
# hex(id(a))
# hex(id(b))


#### BUT THIS DOESN'T WORK IN A SCRIPT
#### Uncomment below, run it as a script, pay very close attention to the comments in main()
#### confusing huh?
# def magic_identity_ball(obj1, obj2):
#     """
#     Returns true if the obj1 and obj2 are the same object,
#         if they have same memory address!
#     """
#     # return id(obj1) == id(obj2)
#     return obj1 is obj2
#
# def magic_equality_ball(value1, value2):
#     """Returns True if the VALUE of value1 and value2 are equal"""
#     return value1 == value2
#
# def main():
#     a = 1024 #outside of cache range, these should be different objects
#     b = 1024 #outside of cache range, these should be different objects
#     print("Creating two new integer objects, a = 1024, b = 1024")
#     print("a == b? magic_equality_ball says: {}".format(magic_equality_ball(a, b)))
#     print("a is b? magic_identity_ball says: {}".format(magic_identity_ball(a, b)))
#     print(a == b) # true, obviously 1024 == 1024
#     print(a is b) # true, the objects are the same! outside of the cache range!
#     print(hex(id(a))) # memory addresses are the same!
#     print(hex(id(b))) # memory addreses are the same!
#     b = 2048 # chance b, does it change a? they are the same object right?
#     print("Changing b = 2048")
#     print("a == b? magic_equality_ball says: {}".format(magic_equality_ball(a, b)))
#     print("a is b? magic_identity_ball says: {}".format(magic_identity_ball(a, b)))
#     print(a == b) # false, 1024 != 2048
#     print(a is b) # false, we didn't change a at all!
#     print(hex(id(a)))
#     print(hex(id(b))) # and now b has a different id!
#     a = 2048 # change a to equal b's value
#     print("Changing a = 2048")
#     print("a == b? magic_equality_ball says: {}".format(magic_equality_ball(a, b)))
#     print("a is b? magic_identity_ball says: {}".format(magic_identity_ball(a, b)))
#     print(a == b) # true, 2048 != 2048
#     print(a is b) # true?
#     print(hex(id(a))) # a and b now have the same id!
#     print(hex(id(b))) # a and b now have the same id!
#
# if __name__ == "__main__":
#     """
#     Not sure what if __name__ == '__main__' does?
#     Check this out: https://www.youtube.com/watch?v=5edEA2YYjLk
#     """
#     main()
