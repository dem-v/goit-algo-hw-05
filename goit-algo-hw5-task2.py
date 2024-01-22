def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    high_val = arr[high]
    mid = 0
    att_cnt = 0

    while low <= high:
        att_cnt += 1
        mid = (high + low) // 2

        # якщо x більше за значення посередині списку, ігноруємо ліву половину
        if arr[mid] < x:
            low = mid + 1
            high_val = arr[mid] if high-low <= 1 else arr[high]

        # якщо x менше за значення посередині списку, ігноруємо праву половину
        elif arr[mid] > x:
            high = mid - 1
            high_val = arr[mid] if high-low <= 1 else arr[high]

        # інакше x присутній на позиції і повертаємо його
        else:
            high_val = arr[mid]
            return att_cnt, high_val

    if high_val < x and high < len(arr) - 1:
        high_val = arr[mid+1]

    # якщо елемент не знайдений
    return (att_cnt, high_val) if (arr[-1] >= x >= arr[0]) else (att_cnt, arr[0]) if x < arr[0] else (att_cnt, None)


arr = [2, 2.23, 2.4, 3, 4, 5.55, 5.56, 10, 15, 40]
print(f"Search for 10, (# of iters, value found): {binary_search(arr, 10)}")
print(f"Search for 5.556, (# of iters, value found): {binary_search(arr, 5.556)}")
print(f"Search for 3.5, (# of iters, value found): {binary_search(arr, 3.5)}")
print(f"Search for 16, (# of iters, value found): {binary_search(arr, 16)}")
print(f"Search for -1, (# of iters, value found): {binary_search(arr, -1)}")
print(f"Search for 41, (# of iters, value found): {binary_search(arr, 41)}")
