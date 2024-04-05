def binary_search(arr, target):
	print("in function, arr is", arr, "target is", target)
	low = 0
	high = len(arr) - 1
	while low <= high:
		mid = (low + high)//2
		print("in loop, low is %d, mid is %d, high is %d"%(low, mid, high))
		if arr[mid] == target:
			return mid
		elif arr[mid] < target:
			low = mid + 1 #you forgot the +1
		else:
			high = mid - 1 #of course you forgot the -1 as well
			
	return -1

arr = [2,7,3,83,8]
target = 4
index = binary_search(arr, target)

if index != -1:
	print("element", target, "found at index", index)
else:
	print("element", target, "not found in list")