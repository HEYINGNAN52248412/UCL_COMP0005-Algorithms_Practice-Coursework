# Bubble Sort: Time: O(N^2), Space: O(1), Stable: Yes
def Bubble_Sort(nums:List[int]):

    for i in range(0, len(nums)):
        #if no switch takes place: the array is already sorted
        swapped = False
        for j in range(0, len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swapped = True
        if not swapped:
            break

    return nums
