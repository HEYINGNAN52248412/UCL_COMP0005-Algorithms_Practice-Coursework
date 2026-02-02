# Merge Sort: Time: O(N log N), Space: O(N), Stable: Yes
def Merge_Two_List(l1:List[int], l2:List[int] ) -> list:
    return_List = []
    i = 0
    j = 0
    while True:
        if i>=len(l1) and j<len(l2):
            return_List.append(l2[j])
            j+=1
        elif j>=len(l2) and i<len(l1):
            return_List.append(l1[i])
            i+=1
        elif l1[i] <= l2[j]:
            return_List.append(l1[i])
            i+=1
        elif l1[i] > l2[j]:
            return_List.append(l2[j])
            j+=1
        else: break

    return return_List

def Merge_Sort(nums:List[int]):
    if len(nums)<=1:
        return nums

    mid = len(nums)//2
    left = nums[:mid]
    right = nums[mid:]

    left = Merge_Sort(left)
    right = Merge_Sort(right)

    return Merge_Two_List(left, right)