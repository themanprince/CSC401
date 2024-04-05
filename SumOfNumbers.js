function sum(n) {
	let sum = 0; //O(1) 1 unit of time
	for(let i = 1; i <= n; ++i) { //this loop will repeat n times
		sum += i; //O(1 * n) - 1 unit of time and will repeat n times because of loop
	}
	return sum; //O(1)
}