# Bucket Sort: Time: O(N + K) avg, Space: O(N + K), Stable: Yes
def Bucket_Sort(nums:List[int]):
    bucket_size = 10
    min_val, max_val = min(nums), max(nums)
    range_val = (max_val - min_val) / bucket_size
    buckets = [[] for _ in range(10)]
    for i in range (len(nums)):
        if range_val == 0:
            index = 0
        else:    
            index = (nums[i] - min_val) //range_val
        if index>= bucket_size:
            index = bucket_size -1

        buckets[index].append(nums[i])

    result = []
    for bucket in buckets:
        bucket.sort()
        result.extend(bucket)

    return result
