from typing import List
from earnings.earning_strategy import EarningStrategy
from models.creator_metrics import CreatorMetrics


class Creator:

    def __init__(self, name: str, metrics: CreatorMetrics):
        self._name = name
        self._metrics = metrics
        self._earning_strategies: List[EarningStrategy] = []

    @property
    def name(self) -> str:
        return self._name

    def add_strategy(self, strategy: EarningStrategy) -> None:
        print(f"Adding strategy to creator {self._name}")
        self._earning_strategies.append(strategy)

    def calculate_total_earnings(self) -> float:
        total = sum(
            strategy.calculate(self._metrics)
            for strategy in self._earning_strategies
        )
        print(f"Total earnings for {self._name} = {total}")
        return total

    def __repr__(self) -> str:
        return f"Creator(name={self._name})"