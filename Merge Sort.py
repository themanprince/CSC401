def merge_sort(arr):
	if len(arr) <= 1:
		return arr
		
	mid = len(arr)//2
	left = merge_sort(arr[:mid])
	right = merge_sort(arr[mid:])
	print("inside merge_sort func, left is", left, "right is", right)
	return merge(left, right)

def merge(left, right):
	print("beginning of merge func, left is", left, "right is", right)
	merged = []
	i = 0
	j = 0
	while i < len(left) and j < len(right):
		print("inside loop, i is %d, j is %d"%(i, j))
		if left[i] <= right[j]:
			merged.append(left[i])
			i += 1
		else:
			merged.append(right[j])
			j += 1
		print("end of if block, merged is", merged)
	merged.extend(left[i:])
	print("just extended merged with left", merged)
	merged.extend(right[j:])
	print("just extended merged with right", merged)
	return merged

arr = [24,6,2]
sorted_arr = merge_sort(arr)
print(sorted_arr)