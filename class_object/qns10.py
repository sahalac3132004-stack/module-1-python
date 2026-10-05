count = 0
num = 2
total = 0

while count < 10:
    is_prime = True
    i = 2

    while i < num:
        if num % i == 0:
            is_prime = False
            break
        i += 1

    if is_prime:
        print(num)
        total += num
        count += 1

    num += 1

print("Sum of first 10 prime numbers:", total)