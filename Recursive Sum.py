def sum(arr): #sum of arr
	if len(arr) == 2:
		return arr[0] + arr[1]
	elif len(arr) == 1:
		return arr[0]
	else:
		mid = len(arr)//2
		return sum(arr[:mid]) + sum(arr[mid:])