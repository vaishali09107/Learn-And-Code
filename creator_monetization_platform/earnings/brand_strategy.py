from earnings.earning_strategy import EarningStrategy
from models.creator_metrics import CreatorMetrics


class BrandStrategy(EarningStrategy):

    def __init__(self, base_amount: float):
        self._base_amount = base_amount

    def calculate(self, metrics: CreatorMetrics) -> float:
        engagement_bonus = metrics.engagement_rate * 100
        return self._base_amount + engagement_bonus