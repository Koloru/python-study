def isValid(s: str):
    map = {}
    map['()'] = s.count('()')
    map['{}'] = s.count('{}')
    map['[]'] = s.count('[]')
    paren = map['()']
    brackets = map['{}']
    braces = map['[]']

    print(paren, brackets, braces)
    # if paren and brackets and braces:
    #     return True
    # return False


print(isValid("([)]"))
print(isValid("(){}[]"))
# print(isValid("(){}{}{{{{{}}}}}[]"))
# print(isValid("(){}{}{{{{{}}}}}[[[[[[[[]]]]]]]]"))

