class School:
    """
    A class to manage student enrollment and grade organization in a school.
    """
    
    def __init__(self) -> None:
        """
        Initializes an empty school with a dictionary to store students by grade
        and a list to track whether a student was successfully added.
        """
        self.students = {}  # Dictionary storing student names categorized by grade
        self.added_status = []  # List tracking successful student additions

    def add_student(self, name: str, grade: int) -> None:
        """
        Adds a student to the school in the specified grade.
        If the student is already in the roster, the addition is marked as unsuccessful.

        Args:
            name (str): The name of the student.
            grade (int): The grade level of the student.
        """
        if name in self.roster():
            self.added_status.append(False)  # Student already exists
        elif grade in self.students:
            self.students[grade].append(name)
            self.added_status.append(True)  # Student successfully added
        else:
            self.students[grade] = [name]
            self.added_status.append(True)  # Student successfully added

    def roster(self) -> list[str]:
        """
        Retrieves a sorted list of all students in the school.
        The students are sorted first by grade, then alphabetically within each grade.

        Returns:
            list[str]: A sorted list of student names.
        """
        sorted_students_by_grade = dict(sorted(self.students.items()))  # Sort by grade
        all_students = [student for grade in sorted_students_by_grade.values() for student in sorted(grade)]
        return all_students

    def grade(self, grade_number: int) -> list[str]:
        """
        Retrieves a list of students in a specific grade, sorted alphabetically.

        Args:
            grade_number (int): The grade level to retrieve students for.

        Returns:
            list[str]: A sorted list of student names in the given grade.
        """
        return sorted(self.students.get(grade_number, []))

    def added(self) -> list[bool]:
        """
        Retrieves the list of statuses indicating whether students were successfully added.

        Returns:
            list[bool]: A list of boolean values where True indicates a successful addition.
        """
        return self.added_status

        