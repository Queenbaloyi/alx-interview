sland_perimeter(grid):
  perimeter = 0
  rows, cols = len(grid), len(grid[0])

  for i in range(rows):
    for j in range(cols):
      if grid[i][j] == 1:
        perimeter   
 += 4

        # Check right and bottom neighbors (if not on edge)
        if j + 1 < cols and grid[i][j + 1] == 1:
          perimeter -= 2
        if i + 1 < rows and grid[i + 1][j] == 1:
          perimeter -= 2

        # Handle edge cases (first/last row/column)
        if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
          perimeter += 1  # Add 1 for each water neighbor on the edge

  return perimeter
