# def is_prime(n):
#     """Returns True if n is a prime number and False otherwise.
#     >>> is_prime(2)
#     True
#     >>> is_prime(16)
#     False
#     >>> is_prime(521)
#     True
#     """
#     def helper(i):
#         if i > (n ** 0.5): # Could replace with i == n
#             return True
#         elif n % i == 0:
#             return False
#         return helper(i + 1)
#     return helper(2)

# def primes_gen(n):
#     """Generates primes in decreasing order.
#     >>> pg = primes_gen(7)
#     >>> list(pg)
#     [7, 5, 3, 2]
#     """
#     "*** YOUR CODE HERE ***"
#     # for i in reversed(range(2, n + 1)):
#     #     if is_prime(i):
#     #         yield i
#     def helper(i):
#         if i > n:
#             return
#         if is_prime(i):
#             yield i
#         yield from helper(i+1)
#     return helper(2)


def stair_ways(n):
    """
    Yields all ways to climb a set of N stairs taking
    1 or 2 steps at a time.

    >>> list(stair_ways(0))
    [[]]
    >>> s_w = stair_ways(4)
    >>> sorted([next(s_w) for _ in range(5)])
    [[1, 1, 1, 1], [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2]]
    >>> list(s_w) # Ensure you're not yielding extra
    []
    """
    "*** YOUR CODE HERE ***"
    if n == 0:
        yield []
    elif n == 1:
        yield [1]
    elif n == 2:
        yield [1, 1]
        yield [2]
    else:
        for i in stair_ways(n - 1):
            yield i + [1]
        for i in stair_ways(n - 2):
            yield i + [2]