from earnings.earning_strategy import EarningStrategy
from models.creator_metrics import CreatorMetrics


class SubscriptionStrategy(EarningStrategy):

    SUBSCRIPTION_PRICE = 2.0

    def calculate(self, metrics: CreatorMetrics) -> float:
        return metrics.subscribers * self.SUBSCRIPTION_PRICE