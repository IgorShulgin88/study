numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
sum_ = 0
primes = []
not_primes = []
i = 0
for i in range(len(numbers)):
    is_prime = True
    sum_ = numbers[i]
    if sum_ < 2:
        continue
    else:
        f = sum_ ** (1 / 2)
    for j in range(2, int(f + 1)):
        if sum_ % j == 0:
            is_prime = False
            break
    if not (is_prime):
        not_primes.append(sum_)
    else:
        primes.append(sum_)
is_prime = True
print('Primes: ', primes)
print('Not primes: ', not_primes)