# Insertion Sort: Time: O(N^2), Space: O(1), Stable: Yes
def insertion_sort (nums: List[int]):
    for i in range(len(nums)):
        for j in range(i, 0, -1):
            if nums[j] < nums[j-1]:
                nums[j-1], nums[j] = nums[j], nums[j-1]
            else: 
                break
