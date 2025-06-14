from ...models.base import MaterialGroupBase
from ...models.models import Drop, Item, Source, Weekday


class Prosperity(MaterialGroupBase):
    @property
    def drop(self) -> Drop:
        return Drop(
            item=Item("Prosperity Books", "https://genshin-impact.fandom.com/wiki/Prosperity_Book"),
            source=Source("Taishan Mansion", "https://genshin-impact.fandom.com/wiki/Taishan_Mansion")
        )

    @property
    def available_on(self) -> list[Weekday]:
        return [Weekday.MON, Weekday.THU, Weekday.SUN]
