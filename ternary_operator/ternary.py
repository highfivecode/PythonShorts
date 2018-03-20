"""
HighFiveCode - https://highfivecode.com/
HFC YouTube Channel: https://www.youtube.com/channel/UCOmiui0ghT5OoVdD1wi4mFA
Send requests to: https://highfivecode.com/suggestions/
History of the ternary:
1. Proposed in PEP 308 7 Feb 2003 https://www.python.org/dev/peps/pep-0308/
2. Accepted Sep 30 2005: https://mail.python.org/pipermail/python-dev/2005-September/056846.html
3. Python3.6 Documentation: https://docs.python.org/3.6/reference/expressions.html#conditional-expressions
Ternary Syntax: A if C else B
This first evaluates C; if it is true, A is evaluated to give the
result, otherwise, B is evaluated to give the result.
"""

# result = A if C else B
# it helps to read it aloud: "result will be A if C is True, else it will be B"

def main():
    result = "I am True" if True else "I am False"
    print("Checking 'result = \"I am true\" if True else \"I am False\" ")
    print("result = {}".format(result))
    result = "I am True" if False else "I am False"
    print("Checking 'result = \"I am True\" if False else \"I am False\" ")
    print("result = {}".format(result))
    
if __name__ == "__main__":
    main()
