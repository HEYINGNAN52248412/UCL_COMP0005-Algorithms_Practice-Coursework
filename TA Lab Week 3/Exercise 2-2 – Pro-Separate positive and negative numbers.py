#solve it with quick sort without sorting the +/- array
class solution:
    def quick_sort_solution(self, nums:list[int])->list:
        i = -1
        for j in range (len(nums)):
            if nums[j]<0:
                i += 1
                nums[j], nums[i] = nums[i], nums[j]
        
        p_pos = i+1
        p_neg = 0

        while p_neg < p_pos and p_pos < len(nums):
            nums[p_neg], nums[p_pos] = nums[p_pos], nums[p_neg]
            #skip the next negative number, we have to keep it
            p_neg += 2
            #just push p_pos 1 step forward: 
            #before the divide point: p_neg it will weave a list of pos-neg
            #after the divide point: p_pos will leave an array of negative numbers after it.

            #if pos numbers are more than the neg numbers, 
            #then when p_neg get the p_pos(p_neg has already done with all the neg-pos switch), the remaining pos numbers will be right after them.
            #if neg numbers are more than the pos numbers, 
            #then p_neg will never catch p_pos--the whole loop stopped cuz p_pos reached the end, when all the pos numbers are thrown back to the front of the list.
            #and there will remain an array of negative numbers after p_neg. the p_pos will be out of bound, and the thing right before it is the negative number array. 
            p_pos += 1

        return nums