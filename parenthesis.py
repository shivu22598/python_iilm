def isValid(s: str)-> bool:
    stack=[]
    mapping={')':'(','}':'{',']':'['}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif(char in mapping):
            if not stack:
                return False
            top=stack.pop()
            if top != mapping[char]:
                return False
    return len(stack) == 0            
s = input("Enter parentheses string: ")
print(isValid(s))