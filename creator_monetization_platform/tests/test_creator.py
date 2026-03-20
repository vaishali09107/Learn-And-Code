from creators.creator import Creator
from earnings.ads_strategy import AdsStrategy
from models.creator_metrics import CreatorMetrics


def test_ads_earnings():
    metrics = CreatorMetrics(views=1000, subscribers=100)
    creator = Creator("Test", metrics)

    creator.add_strategy(AdsStrategy())

    assert creator.calculate_total_earnings() == 50