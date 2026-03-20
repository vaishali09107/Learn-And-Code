from earnings.earning_strategy import EarningStrategy
from models.creator_metrics import CreatorMetrics


class AdsStrategy(EarningStrategy):

    ADS_RATE = 0.05

    def calculate(self, metrics: CreatorMetrics) -> float:
        return metrics.views * self.ADS_RATE