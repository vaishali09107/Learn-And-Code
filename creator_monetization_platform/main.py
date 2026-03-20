from creators.creator import Creator
from earnings.ads_strategy import AdsStrategy
from earnings.subscription_strategy import SubscriptionStrategy
from earnings.brand_strategy import BrandStrategy
from managers.monetization_manager import MonetizationManager
from models.creator_metrics import CreatorMetrics


def main() -> None:

    metrics = CreatorMetrics(
        views=50000,
        subscribers=1200,
        engagement_rate=0.12,
        region="india",
        season="festival",
    )

    creator = Creator("Alex", metrics)

    creator.add_strategy(AdsStrategy())
    creator.add_strategy(SubscriptionStrategy())
    creator.add_strategy(BrandStrategy(5000))

    manager = MonetizationManager()
    manager.add_creator(creator)

    earnings = creator.calculate_total_earnings()

    print(f"Creator Earnings: ${earnings}")
    print(
        f"Platform Earnings: "
        f"${manager.calculate_platform_earnings()}"
    )


if __name__ == "__main__":
    main()