def solution(a, b):
    arr = a[:]
    for elem in b:
        if elem not in a:
            arr.append(elem)
    return sorted(arr)