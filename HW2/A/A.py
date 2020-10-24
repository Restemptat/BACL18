def solution(arr):
	l = 1 #curent length of same figures
	lmax = 1 # max quantity of consecutive elements
	n = len(arr)
	for i in range(n):
		if arr[i] == arr[i-1]:
			l = l+1
		else:
			l = 1
		if l > lmax:
			max = l
	return lmax