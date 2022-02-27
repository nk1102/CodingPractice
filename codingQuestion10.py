def checkPalindrome(str):

    for i in range(0, len(str) // 2):
        if str[i] != str[len(str) - i - 1]:
            return False

    return True


# Driver code
st = str(input())
if (checkPalindrome(st) == True):
    print("true")
else:
    print("false")