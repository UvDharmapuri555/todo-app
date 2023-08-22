import time
series_amount = int(input("Enter a number here to list the Fibonacci Series: ")) - 3
fib_list = [0, 1]
l = 1
h = l - 1
fib_calc = fib_list[l] + fib_list[h]
fib_list.append(fib_calc)
for _ in range(series_amount):
    l = l + 1
    h = l - 1
    fib_calc = fib_list[l] + fib_list[h]
    fib_list.append(fib_calc)
print()
print(f"These are the first {series_amount + 3} numbers of the Fibonacci Series: ")
time.sleep(1)
print(fib_list)
