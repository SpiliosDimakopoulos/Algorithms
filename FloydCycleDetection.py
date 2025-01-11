#O(n) time complexity and O(!) space complexity

class FloydCycleDetection:
    def findDuplicate(self, nums):
        slow = nums[0]
        fast = nums[0]
      
        # Phase 1: Detect the cycle
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Phase 2: Find the entry point of the cycle
        fast = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return fast

'''
nums = [3, 1, 3, 4, 2]
solution = FloydCycleDetection()
print(solution.findDuplicate(nums))
'''
