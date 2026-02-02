"""
Iterative Quick Sort Implementation using a Stack

Logic:
1. Instead of recursion, we use a manual stack to store range tuples (low, high).
2. We continuously pop a range, partition it, and push the left/right sub-ranges back.

----------------------------------------------------------------------------------
WHY WE SKIP SINGLE ELEMENTS (low >= high):
----------------------------------------------------------------------------------
In the `while` loop, we explicitly check `if low < high`. If `low == high` (a single 
element), we do nothing. This is safe because of the "Pivot Invariant".

The Pivot Invariant:
After `partition`, the chosen pivot is placed in its FINAL sorted position. 
It acts as a permanent wall.

The "Sandwich" Effect:
A single element that is skipped is effectively "sandwiched" between two already-fixed 
pivots (or the array boundaries). Since its left neighbor is guaranteed smaller (and fixed) 
and its right neighbor is guaranteed larger (and fixed), the single element itself 
MUST be in the correct position by logic.

Example Trace: [2, 1, 3]
1. Processing range (0, 2): 
   - Pivot is 3. After partition: [2, 1, 3]. 
   - 3 is fixed at index 2.
   - Pushes left range (0, 1) to stack.

2. Processing range (0, 1):
   - Pivot is 1. After partition: [1, 2, 3].
   - 1 is fixed at index 0.
   - Pushes right range (1, 1) to stack (this is the value 2).

3. Processing range (1, 1):
   - logic checks `if 1 < 1`: False. 
   - We skip it.
   - RESULT: The value 2 (at index 1) was never touched directly as a pivot, 
     but it is surrounded by the fixed 1 (left) and fixed 3 (right). 
     It is sorted automatically!
"""

def partition(nums, low, high):
    pivot = nums[high]
    #in case the nums[low] is less than pivot. if we change i = low, then we need to add 1 to it after the switch. 
    #And when we gonna put the pivot to its place, we need to switch it with nums[i]
    i = low-1

    for j in range(low, high):
        if nums[j] < pivot:
            i += 1
            nums[j], nums[i] = nums[i], nums[j]
        
    #do the switch
    nums[i+1], nums[high] = nums[high], nums[i+1]
    return i+1

def Quick_Sort(nums:List[int]) -> list:
    stack = [(0, len(nums)-1)]
    while stack:
        low, high = stack.pop()
        if low < high:
            pivot = partition(nums, low, high)
            left = nums(low, pivot-1)
            right = nums(pivot, high)
            stack.append(left)
            stack.append(right)
    
    return nums