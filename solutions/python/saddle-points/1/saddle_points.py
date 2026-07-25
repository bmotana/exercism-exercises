from typing import List

def saddle_points(matrix: List[list]) -> list:
    """
    Find saddle points in a matrix.
    A saddle point is a number that is both the largest in its row and smallest in its column.
    
    Args:
        matrix: A list of lists representing a matrix
        
    Returns:
        A list of dictionaries containing the coordinates of saddle points
    """
    # Check if matrix is empty
    if not matrix:
        return []
        
    # Check if matrix is irregular (rows of different lengths)
    if len(set([len(matrix_row) for matrix_row in matrix])) != 1:
        raise ValueError("irregular matrix")
        
    coordinates = []
    
    # If matrix is not empty, get the number of columns from the first row
    num_cols = len(matrix[0]) if matrix else 0
    
    # Check each position in the matrix for saddle points
    for row_idx, row in enumerate(matrix):
        for col_idx in range(num_cols):
            current_value = row[col_idx]
            
            # Check if current value is maximum in its row
            if current_value == max(row):
                # Get all values in the current column
                column_values = [matrix[r][col_idx] for r in range(len(matrix))]
                
                # Check if current value is minimum in its column
                if current_value == min(column_values):
                    # Add 1 to indices for 1-based indexing in result
                    coordinates.append({"row": row_idx + 1, "column": col_idx + 1})
    
    return coordinates