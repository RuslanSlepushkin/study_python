def fibonacci_search_recursive(arr: list, target: int, low: int, high: int) -> int:
    if low > high:
        raise ValueError(f"Element not found")

    fib_1 = 0
    fib_2 = 1
    fib = fib_2 + fib_1

    while fib <= (high - low + 1):
        fib_1 = fib_2
        fib_2 = fib
        fib = fib_2 + fib_1

    mid = low + fib_1

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return fibonacci_search_recursive(arr, target, mid + 1, high)
    else:
        return fibonacci_search_recursive(arr, target, low, mid - 1)