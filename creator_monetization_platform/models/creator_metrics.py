from utils.validators import validate_non_negative


class CreatorMetrics:

    def __init__(
        self,
        views: int,
        subscribers: int,
        engagement_rate: float = 0.0,
        region: str = "global",
        season: str = "normal",
    ):
        validate_non_negative(views, "views")
        validate_non_negative(subscribers, "subscribers")

        self._views = views
        self._subscribers = subscribers
        self._engagement_rate = engagement_rate
        self._region = region
        self._season = season

    @property
    def views(self) -> int:
        return self._views

    @property
    def subscribers(self) -> int:
        return self._subscribers

    @property
    def engagement_rate(self) -> float:
        return self._engagement_rate

    @property
    def region(self) -> str:
        return self._region

    @property
    def season(self) -> str:
        return self._season