palindrome_input = input("Enter string: ")
strList = list(palindrome_input)
l = 0
h = len(strList) - 1
x = True

while h > l:
    if strList[l] != strList[h]:
        x = False
    l += 1
    h -= 1
if x:
    print("This string is a palindrome.")
else:
    print("The string is not a palindrome.")