def generate_permutations(elements):
	if len(elements) == 1:
		return [elements]
	
	permutations = []
	for i in range(len(elements)):
		remaining = elements[:i] + elements[i + 1:]
		sub_permutations = generate_permutations(remaining)
		for perm in sub_permutations:
			permutations.append([elements[i]] + perm)
	
	return permutations

elements = [2, 7, 3, 84]
permutations = generate_permutations(elements)
for perm in permutations:
	print(perm)