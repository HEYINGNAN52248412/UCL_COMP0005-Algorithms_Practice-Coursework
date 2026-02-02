# Quick Sort: Time: O(N log N) avg / O(N^2) worst, Space: O(log N), Stable: No
#merge sort: divide then sort
#quick sort: sort then divide
def Quick_Sort(nums:List[int]) -> list:
    if len(nums) <= 1:
        return nums
    pivot = nums[-1]

    #for every element that is not pivot: put them into two arrays
    left = [x for x in nums[:-1] if x <= pivot]
    right = [x for x in nums[:-1] if x >pivot]

    #now every element in left is smaller than that in right.
    #so just use "add" instead of using complex "merge two sorted arrays"
    left = Quick_Sort(left)
    right = Quick_Sort(right)

    return left + [pivot] + right