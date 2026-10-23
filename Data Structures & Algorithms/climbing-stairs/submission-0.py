class Solution:
    def climbStairs(self, n: int) -> int:
        ways_step_one, ways_step_two = 1, 2
        if n == 1 or n == 2 : 
            return n

        for i in range(3,n) : 
            temp = ways_step_one + ways_step_two
            ways_step_one, ways_step_two = ways_step_two, temp
        return ways_step_one + ways_step_two

        