class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # Step 1: Convert times to minutes
        def timeToMinutes(time: str) -> int:
            hours, minutes = map(int, time.split(":"))
            return hours * 60 + minutes
        
        # Convert all times to minutes
        minutes_list = [timeToMinutes(time) for time in timePoints]
        
        # Step 2: Sort the list of times in minutes
        minutes_list.sort()
        
        # Step 3: Initialize the minimum difference as a large number
        min_diff = float('inf')
        
        # Step 4: Compare adjacent times to find the minimum difference
        for i in range(1, len(minutes_list)):
            min_diff = min(min_diff, minutes_list[i] - minutes_list[i-1])
        
        # Step 5: Don't forget the wrap-around difference (between the last and first time)
        # Since the time wraps around at 24 hours, we compare the first and last time as well
        min_diff = min(min_diff, (1440 - minutes_list[-1] + minutes_list[0]))
        
        # Return the minimum difference found
        return min_diff
