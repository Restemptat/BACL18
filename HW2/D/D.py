def solution(n,k):
    print("Case n=", n, "k=", k)
    if n == 1:
        return 1
    if n == 0:
        return 0
    if k == 1:
        return n
    arr = list(range(1, n+1))
    l=0
    arr1 = list()
    while len(arr) > 1:
        for i in range(len(arr)):
            #print(arr[i])
            l+=1
            if l != k:
                arr1.append(arr[i])
            else:
                l = 0
            #print(arr1, l, arr[i])
        arr = arr1
        arr1 = list()		
    return arr[0]

