from typing import Optional

def transpose(text: str) -> str:
   """
   Transposes text by converting rows to columns while maintaining proper spacing.
   
   Args:
       text (str): Multi-line string to transpose
       
   Returns:
       str: Transposed text with proper padding
       
   Example:
       >>> text = "ABC\\nDE"
       >>> transpose(text)
       'AD\\nBE\\nC'
   """
   if not text:
       return ""

   # Split input into lines
   lines = text.split("\n") 
   
   # Find length of longest line
   max_line_length = max(len(line) for line in lines)
   transposed_lines = []

   # Process each column position
   for col_idx in range(max_line_length):
       current_col = []
       
       # Process each row for current column
       for row_idx in range(len(lines)):
           current_row = lines[row_idx]
           
           if col_idx < len(current_row):
               # Character exists at this position
               current_col.append(current_row[col_idx])
           elif row_idx < len(lines) - 1 and _has_longer_subsequent_line(lines, row_idx, col_idx):
               # Add space if there are longer lines after this one
               current_col.append(" ")
           else:
               # Add empty string for padding
               current_col.append("")
               
       transposed_lines.append("".join(current_col))
   
   return "\n".join(transposed_lines)

def _has_longer_subsequent_line(lines: list[str], current_row: int, col_idx: int) -> bool:
   """
   Checks if any subsequent line is long enough to have a character at col_idx.
   
   Args:
       lines (list[str]): List of all lines
       current_row (int): Index of current row being processed  
       col_idx (int): Current column index being checked
       
   Returns:
       bool: True if any subsequent line extends to col_idx
   """
   return col_idx < max(len(lines[i]) for i in range(current_row + 1, len(lines)))