#solve it with merge sort
#divide them into pos_list and neg_list, merge sort both of them, then merge them in requested order
class solution:
    def seperate_pos_and_neg(self, nums:list[int]) ->list:
        pos_list = []
        neg_list = []
        for num in nums:
            if num < 0:
                neg_list.append(num)
            else:
                pos_list.append(num)
        
        pos_list = self.mergeSort(pos_list)
        neg_list = self.mergeSort(neg_list)

        ans = []
        pointer_pos = 0
        pointer_neg = 0
        while p_pos < len(pos_list) and p_neg < len(neg_list):
            ans.append(pos_list[pointer_pos]) 
            ans.append(neg_list[pointer_neg]) 
            pointer_pos += 1
            pointer_neg += 1
            

        if pointer_pos < len(pos_list):
            ans.extend(pos_list[pointer_pos:])
            
        if pointer_neg < len(neg_list):
            ans.extend(neg_list[pointer_neg:])

        return ans
 



    def mergeSort(self, nums:list[int])->list:
        if len(nums) <= 1:
            return nums

        mid = (len(nums))//2
        left = nums[:mid]
        right = nums[mid:]

        left = self.mergeSort(left)
        right = self.mergeSort(right)

        return self.merge_two_sorted_list(left, right)

    def merge_two_sorted_list(self, left:list[int], right:list[int])->list:
        pointer_left = 0
        pointer_right = 0
        ans_list = []
        
        while p_left < len(left) and p_right < len(right):
            if left[pointer_left] <= right[pointer_right]:
                ans_list.append(left[pointer_left])
                pointer_left += 1
            else:
                ans_list.append(right[pointer_right])
                pointer_right += 1

        ans_list.extend(left[pointer_left:])
        ans_list.extend(right[pointer_right:])
        
        return ans_list