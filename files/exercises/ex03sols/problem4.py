nums = [int(x) for x in input("Enter numbers: ").split()]
for i in range(len(nums)-1):
	for j in range(len(nums)-1-i):
		if nums[j] > nums[j+1]:
			nums[j], nums[j+1] = nums[j+1], nums[j]
print(" ".join([str(x) for x in nums]))