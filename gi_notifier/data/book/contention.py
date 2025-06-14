from ...models.base import MaterialGroupBase
from ...models.models import Drop, Item, Source, Weekday


class Contention(MaterialGroupBase):
    @property
    def drop(self) -> Drop:
        return Drop(
            item=Item("Contention Books", "https://genshin-impact.fandom.com/wiki/Contention_Book"),
            source=Source("Blazing Ruins", "https://genshin-impact.fandom.com/wiki/Blazing_Ruins")
        )

    @property
    def available_on(self) -> list[Weekday]:
        return [Weekday.MON, Weekday.THU, Weekday.SUN]
