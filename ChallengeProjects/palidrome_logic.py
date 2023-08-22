n1 = int(input("Enter a number to check for palindrome: "))
n2 = 0
n3 = n1
while n1 > 0:
    remainder = n1 % 10
    n2 = n2 * 10 + remainder
    n1 = n1 // 10

if n2 == n3:
    print("This number is a palindrome.")
else:
    print("This number is not a palindrome.")