# Radix Sort: Time: O(N * K), Space: O(N + K), Stable: Yes
def Radix_Sort(nums:List[int]):
    if not nums: return []

    exp = 1
    max_num = max(nums)
    while exp <= max_num:
        buckets = [[] for _ in range (10)]
        for i in range (len(nums)):
            index = (nums[i]//exp)%10
            buckets[index].append(nums[i])

        new_nums = []
        for bucket in buckets:
            new_nums.extend(bucket)

        nums = new_nums
        exp*=10

    return nums