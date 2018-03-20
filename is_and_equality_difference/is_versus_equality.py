"""
HighFiveCode - https://highfivecode.com/
HFC YouTube Channel: https://www.youtube.com/channel/UCOmiui0ghT5OoVdD1wi4mFA
Send requests to: https://highfivecode.com/suggestions/

a == b evaluates if the VALUES of a and b are the same (value equality)
a is b evualuates if the OBJECTS a and b are the same (reference equality)
"a != b" and "a is not b" do the opposite of the above

Quick Gotcha:
Python caches integers in the range of [-5, 256], also for strings
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
