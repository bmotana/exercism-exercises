from typing import List


class HighScores:
    """
    A class to represent and operate on a list of high scores.

    Attributes:
        scores (List[int]): A list of integer scores.
    """

    def __init__(self, scores: List[int]) -> None:
        """
        Initialize a new HighScores instance.

        Args:
            scores (List[int]): A list of integer scores.
        """
        self.scores = scores

    def latest(self) -> int:
        """
        Get the most recent score from the list.

        Returns:
            int: The latest score (last in the list).
        """
        return self.scores[-1]

    def personal_best(self) -> int:
        """
        Get the highest score achieved.

        Returns:
            int: The highest score in the list.
        """
        return max(self.scores)

    def personal_top_three(self) -> List[int]:
        """
        Get the top three highest scores.

        Returns:
            List[int]: A list of the top three scores, sorted in descending order.
        """
        return sorted(self.scores, reverse=True)[:3]

        