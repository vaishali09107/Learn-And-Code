from typing import List
from creators.creator import Creator


class MonetizationManager:

    def __init__(self):
        self._creators: List[Creator] = []

    def add_creator(self, creator: Creator) -> None:
        self._creators.append(creator)

    def calculate_platform_earnings(self) -> float:
        return sum(
            creator.calculate_total_earnings()
            for creator in self._creators
        )