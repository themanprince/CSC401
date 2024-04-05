def count(arr):
	if len(arr) == 1:
		return 1
	else:
		return 1 + count(arr[1:])