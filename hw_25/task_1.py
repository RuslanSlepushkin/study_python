def bubble_sort(arr: list) -> list:
    n = len(arr)
    start = 0
    end = n - 1
    swap = True

    while swap:
        swap = False

        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swap = True

        if not swap:
            break

        swap = False
        end -= 1

        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swap = True

        start += 1

    return arr