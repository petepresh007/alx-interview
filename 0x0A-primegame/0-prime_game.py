#!/usr/bin/python3
'''a module for number game using Sieve of Eratosthenes in Python'''


def isWinner(x, nums):
    '''a function for prime game'''
    max_number = 10000
    is_prime = [True] * (max_number + 1)
    is_prime[0] = is_prime[1] = False

    # sieve algorithm
    p = 2

    while p * p <= 10000:
        if is_prime[p]:
            for mult_of_num in range(p * p, max_number + 1, p):
                is_prime[mult_of_num] = False
        p += 1

    # extract the prime numbers
    primes = [i for i, prime in enumerate(is_prime) if prime]

    # game simulation
    maria = 0
    ben = 0

    for n in nums:
        # remaining numbers to pick from
        remaining_numbers = set(range(1, n + 1))
        maria_turn = True

        while True:
            prime_picked = False
            # Find the smallest prime in the remaining set
            for prime in primes:
                if prime in remaining_numbers:
                    prime_picked = True
                    # Remove the prime and its multiples
                    multiples = range(prime, n + 1, prime)
                    remaining_numbers.difference_update(multiples)
                    break

            if not prime_picked:
                # No primes left to pick, current player loses
                if maria_turn:
                    ben += 1
                else:
                    maria += 1
                break
            maria_turn = not maria_turn

    if maria > ben:
        return 'Maria'
    elif ben > maria:
        return 'Ben'
    else:
        return None
