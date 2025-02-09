def isprime(n: int) -> bool:
    if n == 0 or n == 1:
        return False
    else:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True


def decrypt(n: int):
    primes = {i for i in range(1, n+1) if isprime(i)}
    divisor = []
    while n > 1:
        for i in primes:
            if n % i == 0:
                divisor.append(i)
                n //= i
                break
    return divisor


if __name__ == "__main__":
    arg = int(input())
    print(decrypt(arg))
