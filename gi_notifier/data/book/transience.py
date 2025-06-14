from ...models.base import MaterialGroupBase
from ...models.models import Drop, Item, Source, Weekday


class Transience(MaterialGroupBase):
    @property
    def drop(self) -> Drop:
        return Drop(
            item=Item("Transience Books", "https://genshin-impact.fandom.com/wiki/Transience_Book"),
            source=Source("Violet Court", "https://genshin-impact.fandom.com/wiki/Violet_Court")
        )

    @property
    def available_on(self) -> list[Weekday]:
        return [Weekday.MON, Weekday.THU, Weekday.SUN]
