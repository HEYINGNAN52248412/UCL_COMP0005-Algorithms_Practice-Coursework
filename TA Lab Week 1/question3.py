def balanced_parenthesis(string):
    stack=[]
    pairs={'(':')', '[':']', '{':'}'}
    for char in string:
        if char in pairs:
            stack.append(char)
        elif char in pairs.value():
            if not stack:
                return False
            top_element = stack.pop
            if pairs[top_element]!=char:
                return False
    
    return len(stack) == 0
        

