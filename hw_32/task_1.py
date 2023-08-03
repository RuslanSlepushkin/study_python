import math
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from datetime import datetime


def is_prime(num: int) -> bool:
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def filter_primes_thread(numbers: list) -> list:
    with ThreadPoolExecutor() as executor:
        results = executor.map(is_prime, numbers)
    return list(results)


def filter_primes_process(numbers: list) -> list:
    with ProcessPoolExecutor() as executor:
        results = executor.map(is_prime, numbers)
    return list(results)


NUMBERS = [
    2,  # prime
    1099726899285419,
    1570341764013157,  # prime
    1637027521802551,  # prime
    1880450821379411,  # prime
    1893530391196711,  # prime
    2447109360961063,  # prime
    3,  # prime
    2772290760589219,  # prime
    3033700317376073,  # prime
    4350190374376723,
    4350190491008389,  # prime
    4350190491008390,
    4350222956688319,
    2447120421950803,
    5,  # prime
]

start_1 = datetime.now()
threadpool_results = filter_primes_thread(NUMBERS)

print("Thread results:", threadpool_results, "Time: ", datetime.now() - start_1)

start_2 = datetime.now()
processpool_results = filter_primes_process(NUMBERS)

print("Process results:", processpool_results, "Time: ", datetime.now() - start_2)
