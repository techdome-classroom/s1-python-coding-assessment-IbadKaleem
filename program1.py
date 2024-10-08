class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
    #    write your code here
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()  # To keep track of visited land masses
        islands_count = 0

        def dfs(r: int, c: int):
            # Check for out-of-bounds and water
            if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visited or grid[r][c] == 'W':
                return
            # Mark the land as visited
            visited.add((r, c))
            # Explore all four directions (up, down, left, right)
            dfs(r + 1, c)  # down
            dfs(r - 1, c)  # up
            dfs(r, c + 1)  # right
            dfs(r, c - 1)  # left

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 'L' and (i, j) not in visited:
                    islands_count += 1  # Found a new island
                    dfs(i, j)  # Explore the entire island

        return islands_count

# Example usage
solution = Solution()
dispatch_1 = [["L", "L", "L", "L", "W"], ["L", "L", "W", "L", "W"], ["L", "L", "W", "W", "W"], ["W", "W", "W", "W", "W"]]
dispatch_2 = [["L", "L", "W", "W", "W"], ["L", "L", "W", "W", "W"], ["W", "W", "L", "W", "W"], ["W", "W", "W", "L", "L"]]

print(solution.getTotalIsles(dispatch_1))  # Output: 1
print(solution.getTotalIsles(dispatch_2))  # Output: 3
                    
        return 0
