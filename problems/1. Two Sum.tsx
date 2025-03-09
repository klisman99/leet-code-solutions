function twoSum(nums: number[], target: number): number[] {
    for (let i = 0; i < nums.length; i++) {
		const validNumIndex = nums.indexOf(target - nums[i]);

		if (validNumIndex !== -1 && validNumIndex != i) {
			return [i, validNumIndex];
		}
	}

	return [];
};