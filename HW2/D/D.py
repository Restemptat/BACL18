def solution(n,k):
	arr = list(range(1, n+1))

	#print(arr)

	l=0
	arr1 = arr
	while len(arr) > 1:
		for i in range(len(arr)):
			l+=1
			if l == 3:
				arr1 = arr1[:i]+arr1[i+1:]
				l=1
			print(arr1)
		arr = arr1		
	return arr[0]
