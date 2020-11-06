def solution(arr):
	l = 1 #curent length of same figures
	lmax = 1 # max quantity of consecutive elements
	n = len(arr)
	if n == 1:
		return 1
	else:
		for i in range(n-1):
			if arr[i+1] == arr[i]:
				l = l+1
			else:
				l = 1
			if l > lmax:
				lmax = l
	return lmax