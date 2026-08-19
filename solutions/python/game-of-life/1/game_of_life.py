def tick(matrix: list[list[int]]) -> list[list[int]]:
    """Return the next generation of a Conway's Game of Life board."""
    if not matrix:
        return []

    rows = len(matrix)
    cols = len(matrix[0])
    next_matrix: list[list[int]] = []

    for row in range(rows):
        next_row: list[int] = []
        for col in range(cols):
            live_neighbors = sum(
                matrix[neighbor_row][neighbor_col]
                for neighbor_row in range(max(0, row - 1), min(rows, row + 2))
                for neighbor_col in range(max(0, col - 1), min(cols, col + 2))
                if (neighbor_row, neighbor_col) != (row, col)
            )
            cell_is_alive = matrix[row][col] == 1
            next_row.append(
                int(live_neighbors == 3 or (cell_is_alive and live_neighbors == 2))
            )
        next_matrix.append(next_row)

    return next_matrix

