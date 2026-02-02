def Palindrome_Checker(s):
    if not s:
        return True

    string = s.lower()
    n = len(string)

    left = 0
    right = n-1

    while left<right:
            if string[left] == string[right]:
                return False
            left+=1
            right-=1

    return True


    

