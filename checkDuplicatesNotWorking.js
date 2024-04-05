function checkForDuplicate(Array) {
	for(let i = 0; i <= Array.length; ++i) { //the loop runs for n times
		const tempArray = Array.slice(i + 1); //O(1 * n) - the statement will run for 1 unit time mul by n
		if(tempArray.indexOf(Array[i]) !== -1) { //O(n * n) - the function indexOf() will run n times for tempArr and also loop for n times because of loop above
			return true; //O(1 * n) the statement will run O(1) times and will run n times because of loop
		}
	}
	
	return false; // O(1) - repeated only one time because it is outside loop
}

console.log(checkForDuplicate([1,4,1,2,6,3,7]));