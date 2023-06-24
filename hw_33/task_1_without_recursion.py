import asyncio
from multiprocessing import Pool
from datetime import datetime


async def fibonacci_async(n: int) -> int:
    if n <= 1:
        return n

    fib_minus_2 = 0
    fib_minus_1 = 1
    fib = 0

    for _ in range(2, n + 1):
        fib = fib_minus_2 + fib_minus_1
        fib_minus_2 = fib_minus_1
        fib_minus_1 = fib

    return fib


async def factorial_async(n: int) -> int:
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


async def square_async(n: int) -> int:
    return pow(n, 2)


async def cube_async(n: int) -> int:
    return pow(n, 3)


async def calculate_results_async(n: int) -> tuple:
    return (
        await fibonacci_async(n),
        await factorial_async(n),
        await square_async(n),
        await cube_async(n),
    )


async def main_async() -> tuple:
    numbers = range(1, 11)
    tasks = [calculate_results_async(n) for n in numbers]
    results = await asyncio.gather(*tasks)

    fib_list_async = list()
    fac_list_async = list()
    squ_list_async = list()
    cub_list_async = list()

    for result in results:
        fib, fac, squ, cub = result
        fib_list_async.append(fib)
        fac_list_async.append(fac)
        squ_list_async.append(squ)
        cub_list_async.append(cub)

    return fib_list_async, fac_list_async, squ_list_async, cub_list_async


def fibonacci_mul(n: int) -> int:
    if n <= 1:
        return n

    fib_minus_2 = 0
    fib_minus_1 = 1
    fib = 0

    for _ in range(2, n + 1):
        fib = fib_minus_2 + fib_minus_1
        fib_minus_2 = fib_minus_1
        fib_minus_1 = fib

    return fib


def factorial_mul(n: int) -> int:
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


def square_mul(n: int) -> int:
    return pow(n, 2)


def cube_mul(n: int) -> int:
    return pow(n, 3)


def calculate_results_mul(n: int) -> tuple:
    return fibonacci_mul(n), factorial_mul(n), square_mul(n), cube_mul(n)


def main_mul() -> tuple:
    numbers = range(1, 11)

    with Pool(4) as pool:
        results = pool.map(calculate_results_mul, numbers)

    fib_list_mul = list()
    fac_list_mul = list()
    squ_list_mul = list()
    cub_list_mul = list()

    for result in results:
        fib, fac, squ, cub = result
        fib_list_mul.append(fib)
        fac_list_mul.append(fac)
        squ_list_mul.append(squ)
        cub_list_mul.append(cub)

    return fib_list_mul, fac_list_mul, squ_list_mul, cub_list_mul


if __name__ == "__main__":
    start_async = datetime.now()
    func_async = asyncio.run(main_async())
    end_async = datetime.now()
    print(
        f"Result asyncio:\nfibonacci - {func_async[0]}\nfactorial - {func_async[1]}\nsquare - {func_async[2]}\n"
        f"cube - {func_async[3]}\nTime - {end_async - start_async}\n"
    )

    start_mul = datetime.now()
    func_mul = main_mul()
    end_mul = datetime.now()
    print(
        f"Result multiprocessing:\nfibonacci - {func_mul[0]}\nfactorial - {func_mul[1]}\nsquare - {func_mul[2]}\n"
        f"cube - {func_mul[3]}\nTime - {end_mul - start_mul}"
    )
