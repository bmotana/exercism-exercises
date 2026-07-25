class Garden:
    """
    Represents a garden with plants assigned to students.
    
    This class manages the mapping between students and their assigned plants
    based on a diagram representation of the garden.
    """
    
    # Default list of students in alphabetical order
    STUDENTS = [
        "Alice", "Bob", "Charlie", "David", "Eve", "Fred",
        "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"
    ]
    
    # Mapping from diagram characters to plant names
    PLANT_DIAGRAM_ENCODING = {
        "G": "Grass",
        "C": "Clover",
        "R": "Radishes",
        "V": "Violets"
    }
    
    def __init__(self, diagram: str, students: list = None) -> None:
        """
        Initialize a Garden object with a diagram and optional student list.
        
        Args:
            diagram (str): A multi-line string representing the garden layout.
                           Each character represents a plant type.
            students (list, optional): A custom list of student names. If provided,
                                      replaces the default student list.
        """
        if students:
            self.STUDENTS = sorted(students)
        self.diagram = self._make_rows(diagram)
    
    def plants(self, student: str) -> list:
        """
        Get the list of plants assigned to a specific student.
        
        Each student is assigned 4 plants - 2 plants from each row of the garden,
        positioned according to the student's position in the alphabetically sorted list.
        
        Args:
            student (str): The name of the student whose plants should be returned.
            
        Returns:
            list: A list of plant names (strings) assigned to the student.
            
        Raises:
            ValueError: If the student name is not in the list of students.
        """
        try:
            student_index = self.STUDENTS.index(student)
        except ValueError:
            raise ValueError(f"Student '{student}' not found in the garden's student list")
        
        flowers = []
        for row in self.diagram:
            # Each student gets 2 plants per row
            start_index = student_index * 2
            end_index = start_index + 2
            
            # Get the plant codes for this student in the current row
            student_flowers = row[start_index:end_index]
            
            # Convert codes to plant names and add to result list
            flowers.extend([self.PLANT_DIAGRAM_ENCODING[flower] for flower in student_flowers])
        
        return flowers
    
    def _make_rows(self, diagram: str) -> list:
        """
        Convert the diagram string into a list of rows.
        
        Args:
            diagram (str): A multi-line string representing the garden layout.
        
        Returns:
            list: A list of strings, each representing a row in the garden.
        """
        # Split the diagram into rows and remove any leading/trailing whitespace
        return [row.strip() for row in diagram.split("\n") if row.strip()]