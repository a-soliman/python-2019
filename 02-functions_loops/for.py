primes = [2, 3, 5, 7, 11]

for prime in primes:
    print(prime)


for i in range(len(primes)):
    print(primes[i])


friends = {
    "jack": 6,
    "mike": 3,
    "ron": 4
}

for friend in friends:
    print(friend)

for num in range(2, 10):
    if (num % 2 is 0):
        print("{} is even".format(num))
    else:
        print("{} is an odd.".format(num))
