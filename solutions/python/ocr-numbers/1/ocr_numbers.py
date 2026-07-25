DIGIT_MAP = {
    " _ | ||_|   ": "0",
    "     |  |   ": "1",
    " _  _||_    ": "2",
    " _  _| _|   ": "3",
    "   |_|  |   ": "4",
    " _ |_  _|   ": "5",
    " _ |_ |_|   ": "6",
    " _   |  |   ": "7",
    " _ |_||_|   ": "8",
    " _ |_| _|   ": "9",
}

def convert(input_grid: list) -> str:
    """convert binary fonts to a string of numbers."""
    
    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    if any(len(row) % 3 != 0 for row in input_grid):
        raise ValueError("Number of input columns is not a multiple of three")
    
    num_lines = len(input_grid) // 4
    num_digits_per_line = len(input_grid[0]) // 3
    
    result_lines = []
    
    for i in range(num_lines):
        digits = []
        for j in range(num_digits_per_line):
            digit_str = "".join(
                input_grid[i * 4 + k][j * 3 : (j + 1) * 3] for k in range(4)
            )
            digits.append(DIGIT_MAP.get(digit_str, "?"))
        result_lines.append("".join(digits))
    
    return ",".join(result_lines)
